import pytest
from antlr4 import InputStream, CommonTokenStream
from sql_to_lnh.generated.SQLiteLexer import SQLiteLexer
from sql_to_lnh.generated.SQLiteParser import SQLiteParser
from sql_to_lnh.Visitor import Visitor
from typing import Dict, List, Tuple


def prepare_for_visit(sql_statement: str):
    # Лексический анализ
    input_stream = InputStream(sql_statement)
    lexer = SQLiteLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # Парсинг
    parser = SQLiteParser(tokens)
    ast = parser.parse()

    # Создание Visitor и передача ему AST
    visitor = Visitor()
    return visitor, ast


def extract_names(named_values):
    return list(map(lambda c: c['name'], named_values))


@pytest.mark.parametrize('sql_statement, expected_columns, expected_tables, expected_bind_names, expected_literals', [
    ('SELECT u, du FROM graph_nodes ORDER BY u ASC LIMIT :foo;', ['u', 'du'], ['graph_nodes'], ['foo'], []),
    ('SELECT t.col1, col2 as col FROM some_table AS t ORDER BY u LIMIT 1;', ['col1', 'col2'], ['some_table'], [], [1]),
    ('SELECT * FROM some_table;', ['*'], ['some_table'], [], []),
    ('SELECT t.* FROM some_table AS t WHERE col1 = :foo;', ['*'], ['some_table'], ['foo'], []),
    ('SELECT * FROM table1, table2;', ['*'], ['table1', 'table2'], [], []),
])
def test_visitor_select(sql_statement, expected_columns, expected_tables, expected_bind_names, expected_literals):
    visitor, ast = prepare_for_visit(sql_statement)
    res = visitor.visit(ast)
    assert len(res) == 1
    res = res[0]
    assert res['stmt_type'] == 'select'
    assert extract_names(res['columns']) == expected_columns
    assert extract_names(res['tables']) == expected_tables
    assert res['bind_names'] == expected_bind_names
    assert res['literals'] == expected_literals


@pytest.mark.parametrize('sql_statement, expected_columns, expected_name, expected_clauses, expected_exprs', [
    ('INSERT INTO graph_nodes(u, pu, eQ, du, color) VALUES (0, 1, 2, 3, 4);',
     ['u', 'pu', 'eQ', 'du', 'color'], 'graph_nodes', [['0', '1', '2', '3', '4']], [0, 1, 2, 3, 4]),
    ('INSERT INTO graph_nodes(u, pu, eQ, du, color) VALUES (:u, :pu, :eQ, :du, :color);',
     ['u', 'pu', 'eQ', 'du', 'color'], 'graph_nodes', [[':u', ':pu', ':eQ', ':du', ':color']], ['u', 'pu', 'eQ', 'du', 'color']),
    ('INSERT INTO graph_nodes(u, pu, eQ, du, color) VALUES (0, 1, 2, 3, 4), (:u, :pu, :eQ, :du, :color);',
     ['u', 'pu', 'eQ', 'du', 'color'], 'graph_nodes', [['0', '1', '2', '3', '4'], [':u', ':pu', ':eQ', ':du', ':color']], [0, 1, 2, 3, 4, 'u', 'pu', 'eQ', 'du', 'color'])
])
def test_visitor_insert(sql_statement, expected_columns, expected_name, expected_clauses, expected_exprs):
    visitor, ast = prepare_for_visit(sql_statement)
    res = visitor.visit(ast)
    assert len(res) == 1
    res = res[0]
    assert res['stmt_type'] == 'insert'
    assert res['name'] == expected_name
    assert res['insert_columns'] == expected_columns
    assert res['insert_clause'] == expected_clauses
    assert res['exprs'] == expected_exprs


@pytest.mark.parametrize('sql_statement, table_name, expected_columns, primary_key', [
    ('''
CREATE TABLE table1 (
    col1 INT4 PRIMARY KEY,
    col2 INT2 NOT NULL,
    col3 INT2 NOT NULL
) WITHOUT ROWID;''', 'table1', [('col1', 'unsigned int', 4), ('col2', 'unsigned int', 2), ('col3', 'unsigned int', 2)],
     ['col1']),
    ('''
CREATE TABLE table2 (
    col1 INT4 NOT NULL,
    col2 INT2 NOT NULL,
    col3 INT2 NOT NULL,
    PRIMARY KEY (col1, col2)
) WITHOUT ROWID;''', 'table2', [('col1', 'unsigned int', 4), ('col2', 'unsigned int', 2), ('col3', 'unsigned int', 2)],
     ['col1', 'col2']),
])
def test_visitor_create_table(sql_statement, table_name, expected_columns: List[Tuple[str, str, int]],
                              primary_key: List[str]):
    visitor, ast = prepare_for_visit(sql_statement)
    res = visitor.visit(ast)
    assert len(res) == 1
    res = res[0]
    assert res['stmt_type'] == 'create_table'
    assert res['name'] == table_name
    assert res['PK'] == primary_key
    type_by_name = {c['name']: c['type'] for c in res['columns']}
    for column_name, column_type, type_size in expected_columns:
        assert column_name in type_by_name
        assert type_by_name[column_name]['name'] == column_type
        assert type_by_name[column_name]['size'] == type_size


@pytest.mark.parametrize('sql_statement, expected_return_value', [('', None)])
def test_visitor_empty_line(sql_statement, expected_return_value):
    visitor, ast = prepare_for_visit(sql_statement)
    res = visitor.visit(ast)
    assert res == expected_return_value


@pytest.mark.parametrize('sql_statement', [
    ('''
CREATE TABLE table1 (
    col1 INT4 PRIMARY KEY,
    col1 INT2 NOT NULL
) WITHOUT ROWID;'''),
    ('''
CREATE TABLE table1 (
    col1 INT4 NOT NULL,
    col2 INT2 NOT NULL
) WITHOUT ROWID;'''),
    ('''
CREATE TABLE table2 (
    col1 INT4 NOT NULL,
    col2 INT2 NOT NULL,
    col3 INT2 NOT NULL,
    PRIMARY KEY (col1, col4)
) WITHOUT ROWID;'''),
    ('''
SELECT customer_name, city
FROM customers
WHERE country = 'USA'
UNION
SELECT name, location
FROM stores
WHERE state = 'CA';'''),
    ('SELECT * FROM users WHERE id = ?;')
])
def test_visitor_raises_exceptions(sql_statement):
    with pytest.raises(RuntimeError):
        visitor, ast = prepare_for_visit(sql_statement)
        visitor.visit(ast)


@pytest.mark.parametrize('sql_statement, expected_columns', [
    ('''
CREATE TABLE table1 (
    col1 TINYINT PRIMARY KEY,
    col2 SMALLINT NOT NULL,
    col3 MEDIUMINT NOT NULL,
    col4 INTEGER NOT NULL,
    col5 BIGINT NOT NULL,
    col6 BOOLEAN NOT NULL,
    col7 INT NOT NULL
) WITHOUT ROWID;''', [('col1', 'unsigned int', 1), ('col2', 'unsigned int', 2), ('col3', 'unsigned int', 3),
                      ('col4', 'unsigned int', 4), ('col5', 'unsigned int', 8), ('col6', 'bool', 1),
                      ('col7', 'unsigned int', 4)])
])
def test_visitor_type_converter_check(sql_statement: str, expected_columns: List[Tuple[str, str, int]]):
    visitor, ast = prepare_for_visit(sql_statement)
    res = visitor.visit(ast)
    assert len(res) == 1
    res = res[0]
    assert res['stmt_type'] == 'create_table'
    type_by_name = {c['name']: c['type'] for c in res['columns']}
    for column_name, column_type, type_size in expected_columns:
        assert column_name in type_by_name
        assert type_by_name[column_name]['name'] == column_type
        assert type_by_name[column_name]['size'] == type_size


@pytest.mark.parametrize('sql_statement, exception_message', [
    ('''
CREATE TABLE table1 (
    col1 STRING PRIMARY KEY
) WITHOUT ROWID;''', "Type 'STRING' is not supported yet."),
    ('''
CREATE TABLE table1 (
    col1 INTOGER NOT NULL
) WITHOUT ROWID;''', "Unrecognized type 'INTOGER'!")
])
def test_visitor_missing_types(sql_statement: str, exception_message: str):
    with pytest.raises(RuntimeError) as e_info:
        visitor, ast = prepare_for_visit(sql_statement)
        visitor.visit(ast)
    assert str(e_info.value) == exception_message
