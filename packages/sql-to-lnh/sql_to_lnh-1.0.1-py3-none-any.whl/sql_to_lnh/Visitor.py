from sql_to_lnh.generated.SQLiteParser import SQLiteParser
from sql_to_lnh.generated.SQLiteParser import SQLiteParser as P
from sql_to_lnh.generated.SQLiteParserVisitor import SQLiteParserVisitor
from .TypeConverter import TypeConverter
from typing import Dict, List, Optional
import copy


class Visitor(SQLiteParserVisitor):
    '''
    The `Visitor` class is responsible for visiting the parse tree of an SQL statement and extracting relevant information. It uses the `SQLiteParserVisitor` class as a base and overrides methods to handle specific elements of the parse tree.

    The `Visitor` class maintains a context dictionary (`self.ctx`) that stores information about the statement being visited. This information includes:

    - `bind_names`: A list of bind parameter names used in the statement.
    - `literals`: A list of literal values used in the statement.
    - `exprs`: A list of expressions used in the statement.
    - `stmt_type`: The type of the statement (e.g., `create_table`, `select`, `insert`).
    - `SQL`: The source interval of the statement in the original SQL text.
    - `name`: The name of the table being referenced in the statement.
    - `columns`: A list of column definitions for the table.
    - `PK`: A list of primary key columns for the table.
    - `insert_columns`: A list of columns to be inserted into the table.
    - `insert_clause`: A list of rows to be inserted into the table.
    - `tables`: A list of tables referenced in the `SELECT` statement.
    - `columns`: A list of columns selected in the `SELECT` statement.

    The `Visitor` class provides methods for visiting different elements of the parse tree, such as `create_table_stmt`, `select_stmt`, `insert_stmt`, and others. These methods extract relevant information from the parse tree and update the context dictionary accordingly.

    The context dictionary can be used to generate C++ code that corresponds to the SQL statement being visited.
    '''

    def __init__(self):
        self.ctx: Dict = {'bind_names': [], 'literals': [], 'exprs': []}

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate: List, next_result: Optional[List]):
        if next_result is None or next_result == []:
            return aggregate
        else:
            aggregate.append(copy.deepcopy(next_result))
            return aggregate

    def visitParse(self, ctx: P.ParseContext):
        if ctx.sql_stmt_list():
            return self.visitSql_stmt_list(ctx.sql_stmt_list(0))
        return None

    def visitSql_stmt(self, ctx: P.Sql_stmtContext) -> Dict[str, List]:
        self.ctx: Dict = {'bind_names': [], 'literals': [], 'exprs': []}
        if ctx.create_table_stmt():
            return self.visitCreate_table_stmt(ctx.create_table_stmt())
        if ctx.select_stmt():
            return self.visitSelect_stmt(ctx.select_stmt())
        if ctx.insert_stmt():
            return self.visitInsert_stmt(ctx.insert_stmt())
        raise RuntimeError("This statement is not supported yet!")

    def visitCreate_table_stmt(self, ctx):
        self.ctx['stmt_type'] = 'create_table'
        self.ctx['SQL'] = ctx.getSourceInterval()
        self.ctx['name'] = self.visitTable_name(ctx.table_name())
        col_list = []
        self.ctx['PK'] = []

        for col in ctx.column_def():
            col: P.Column_defContext
            obj = self.visitColumn_def(col)
            if obj['name'] in map(lambda c: c['name'], col_list):
                raise RuntimeError(f"Name '{obj['name']}' is already defined!")
            col_list.append(obj)
            # Check if the column is defined as a PK
            pk_cons_maybe = list(filter(lambda constraint: constraint.PRIMARY_() != None, col.column_constraint()))
            if pk_cons_maybe:
                self.ctx['PK'].append(obj['name'])

        self.ctx['columns'] = col_list
        self.ctx['orig_columns'] = col_list[:]

        # If no columns had PK constraint, then there should be a table PK constraint
        if not self.ctx['PK']:
            # Primary key  table constraint is the one that has a `PRIMARY` keyword. It is either present at [0] index or the list is empty
            pk_maybe = list(filter(lambda constraint: constraint.PRIMARY_() != None, ctx.table_constraint()))
            if pk_maybe:
                pk: P.Table_constraintContext = pk_maybe[0]
                pk_lst = []
                for col in pk.indexed_column():
                    name = self.visitIndexed_columnPK(col)
                    if name in map(lambda c: c['name'], col_list):
                        pk_lst.append(name)
                    else:
                        raise RuntimeError(f"Primary Key '{name}' not found in defined columns!")
                self.ctx['PK'] = pk_lst
            else:
                raise RuntimeError("Primary Key is not defined!")

        return self.ctx

    def visitTable_name(self, ctx: P.Table_nameContext):
        return ctx.getText()

    def visitAny_name(self, ctx: P.Any_nameContext):
        return ctx.getText()

    def visitColumn_def(self, ctx: P.Column_defContext):
        col = {'name': self.visitColumn_name(ctx.column_name()),
               'type': self.visitType_name(ctx.type_name())}
        return col

    def visitColumn_name(self, ctx: P.Column_nameContext):
        return ctx.getText()

    def visitType_name(self, ctx: P.Type_nameContext):
        if ctx.name(0) is not None:
            name = self.visitName(ctx.name(0))
            return TypeConverter.convert(name)
        else:
            return None

    def visitName(self, ctx: P.NameContext):
        return ctx.getText()

    def visitIndexed_columnPK(self, ctx: P.Indexed_columnContext):
        return self.visitColumn_name(ctx.column_name())

    def visitInsert_stmt(self, ctx: P.Insert_stmtContext):
        self.ctx['stmt_type'] = 'insert'
        self.ctx['SQL'] = ctx.getSourceInterval()
        self.ctx['name'] = self.visitTable_name(ctx.table_name())
        self.ctx['insert_columns'] = list(map(lambda x: self.visitColumn_name(x), ctx.column_name()))
        self.ctx['insert_clause'] = self.visitValues_clause(ctx.values_clause())
        return self.ctx

    def visitValues_clause(self, ctx: P.Values_clauseContext):
        rows: List[P.Value_rowContext] = ctx.value_row()
        insert_clause = []
        for row in rows:
            row_data = row.expr()
            if len(row_data) != len(self.ctx['insert_columns']):
                raise RuntimeError("Insert row elements must match insert columns")
            inserted_row = []
            for e in row.expr():
                inserted_row.append(self.visitExpr(e))
            insert_clause.append(inserted_row)
        return insert_clause

    def visitSelect_stmt(self, ctx: P.Select_stmtContext):
        self.ctx['stmt_type'] = 'select'
        self.ctx['SQL'] = ctx.getSourceInterval()
        if len(ctx.select_core()) != 1:
            raise RuntimeError("Only one select core is currently supported!")
        core = self.visitSelect_core(ctx.select_core(0))
        self.ctx.update(core)
        if ctx.limit_stmt():
            for e in ctx.limit_stmt().expr():
                self.visitExpr(e)
        return self.ctx

    def visitSelect_core(self, ctx: P.Select_coreContext):
        core = {
            'columns': list(map(lambda res_col: self.visitResult_column(res_col), ctx.result_column())),
            'tables': []
        }
        for table in ctx.table_or_subquery():
            core['tables'].append(self.visitTable_or_subquery(table))
        for e in ctx.expr():
            self.visitExpr(e)
        return core

    def visitResult_column(self, ctx: P.Result_columnContext):
        if ctx.STAR():
            col = {'name': '*'}  # column with a name '*' will be a special case
            if ctx.table_name():
                col['table'] = self.visitTable_name(ctx.table_name())
            return col
        expr: P.ExprContext = ctx.expr()
        if expr.column_name() is None:
            raise RuntimeError("There needs to be a column name in select")
        col = {'name': self.visitColumn_name(expr.column_name())}
        if expr.table_name():
            col['table'] = self.visitTable_name(expr.table_name())
        if ctx.column_alias():
            col['alias'] = self.visitColumn_alias(ctx.column_alias())
        return col

    def visitColumn_alias(self, ctx: P.Column_aliasContext):
        return ctx.getText()

    def visitTable_or_subquery(self, ctx: P.Table_or_subqueryContext):
        if ctx.table_name() is None:
            raise RuntimeError("Currently only a single table search is supported")
        table = {'name': self.visitTable_name(ctx.table_name())}
        if ctx.table_alias() is not None:
            table['alias'] = self.visitColumn_alias(ctx.table_alias())
        return table

    def visitExpr(self, ctx: P.ExprContext):
        if ctx.literal_value():
            literal_value = int(ctx.getText())
            self.ctx['literals'].append(literal_value)
            self.ctx['exprs'].append(literal_value)

        if ctx.BIND_PARAMETER():
            if ctx.getText()[0] == '?':
                raise RuntimeError(f"Only named parameters are supported!")
            bind_identifier = ctx.getText()[1:]
            self.ctx['bind_names'].append(bind_identifier)
            self.ctx['exprs'].append(bind_identifier)
        for e in ctx.expr():
            self.visitExpr(e)
        return ctx.getText()
