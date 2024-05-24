import pytest
import re
from sql_to_lnh.CodeGenerator import CodeGenerator


@pytest.fixture(scope='module')
def code_generator():
    code_gen = CodeGenerator('test.db')
    yield code_gen
    code_gen.close()

@pytest.fixture(scope='function')
def code_generator_fun():
    code_gen = CodeGenerator('test2.db')
    yield code_gen
    code_gen.close()

@pytest.mark.parametrize('sql_statement, expected_code', [
(
"""
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
""",
"""
struct Graph_nodes {
  int struct_number;
  constexpr Graph_nodes(int struct_number) : struct_number(struct_number) {}
  static const uint32_t adj_c_bits = 32;
  static const uint32_t idx_max = (1ull << adj_c_bits) - 1;

  STRUCT(Key0) {
    unsigned int index: 32 = 0;
    unsigned int u: 32;
  };
  STRUCT(Key1) {
    unsigned int index: 32 = idx_max - 0;
    unsigned int u: 32;
  };
  STRUCT(Val0) {
    unsigned int pu: 32;
    bool eQ: 8;
    unsigned int non: 24 = 0;
  };
  STRUCT(Val1) {
    unsigned int du: 32;
    unsigned int color: 24;
    unsigned int non: 8 = 0;
  };
  #ifdef __riscv64__
  DEFINE_DEFAULT_KEYVAL(Key0, Val0)
  DEFINE_KEYVAL(Key1, Val1)
  #endif
};

constexpr Graph_nodes GRAPH_NODES(1);
"""),
(
"""
SELECT u, du FROM graph_nodes WHERE du > u ORDER BY u DESC LIMIT :foo;
""",
"""
STRUCT(q_2f414b338_record) {
  unsigned int u: 32;
  unsigned int du: 32;
  [[gnu::always_inline]] bool operator==(const q_2f414b338_record rhs) {
    return ((u == rhs.u) && (du == rhs.du));
  }
};
#ifdef __riscv64__
struct q_2f414b338_sentinel {};
struct q_2f414b338_iterator {
  bool terminated = false;
  bool found_res = false;
  int comp_result = 0;
  q_2f414b338_record res;
  Graph_nodes obj2;
  Handle<Graph_nodes::Key0, Graph_nodes::Val0> cur;
  unsigned int foo;
  unsigned int reg1;
  Handle<Graph_nodes::Key1, Graph_nodes::Val1> group1;
  [[gnu::always_inline]] q_2f414b338_iterator(Graph_nodes obj2, Handle<Graph_nodes::Key0, Graph_nodes::Val0> cur, unsigned int foo) : obj2(obj2), cur(cur), foo(foo), reg1(foo) {
    get_record();
  }

  [[gnu::always_inline]] void get_record() {
  mark_5:
    if (found_res)
      return;
    group1 = obj2.search(  Graph_nodes::Key1{ .u = cur.key().u });
    comp_result = group1.value().du - cur.key().u;
    if (comp_result < 0 || comp_result == 0) {
      goto mark_12;
    }
    res = { .u = cur.key().u, .du =  group1.value().du };
    found_res = true;
    reg1--;
    if (reg1 == 0) {
      goto mark_13;
    }
  mark_12:
    cur = obj2.nsm(Graph_nodes::Key0{.index = 0, .u = cur.key().u});
    cur = obj2.search(  Graph_nodes::Key0{.index = 0, .u = cur.key().u});
    if ((bool) cur) {
      goto mark_5;
    }
  mark_13:
    terminated = true;
    return;
  }

  [[gnu::always_inline]] q_2f414b338_record operator*() const {
    return res;
  }

  [[gnu::always_inline]] q_2f414b338_iterator& operator++() {
    found_res = false;
    if (terminated) {
      return *this;
    }
    get_record();
    return *this;
  }

  [[gnu::always_inline]] bool operator==(const q_2f414b338_iterator rhs) {
    assert(obj2.struct_number == rhs.obj2.struct_number);
    return ((((bool) cur == false) && ((bool) rhs.cur == false)) || (**this == *rhs));
  }

  [[gnu::always_inline]] bool operator==(const q_2f414b338_sentinel rhs) {
    return ((found_res == false) && (((bool) cur == false) || (terminated)));
  }
};
struct q_2f414b338_range {
  Graph_nodes obj0;
  unsigned int foo;
  [[gnu::always_inline]] q_2f414b338_range(Graph_nodes obj0, unsigned int foo) : obj0(obj0), foo(foo) {}
  [[gnu::always_inline]] auto begin() {return q_2f414b338_iterator(obj0, obj0.get_last(), foo);}
  [[gnu::always_inline]] auto end() {return q_2f414b338_sentinel{};}
};
#endif
"""),
(
"""
SELECT nodes.color FROM graph_nodes AS nodes WHERE color > :arg AND u < 3 LIMIT 5;
""",
"""
STRUCT(q_c346a6a29_record) {
  unsigned int nodes_color: 24;
  [[gnu::always_inline]] bool operator==(const q_c346a6a29_record rhs) {
    return ((color == rhs.color));
  }
};
#ifdef __riscv64__
struct q_c346a6a29_sentinel {};
struct q_c346a6a29_iterator {
  bool terminated = false;
  bool found_res = false;
  int comp_result = 0;
  q_c346a6a29_record res;
  Graph_nodes obj1;
  Handle<Graph_nodes::Key0, Graph_nodes::Val0> cur;
  unsigned int arg;
  unsigned int reg1 = 5;
  unsigned int reg2 = 3;
  Handle<Graph_nodes::Key1, Graph_nodes::Val1> group1;
  unsigned int reg4;
  [[gnu::always_inline]] q_c346a6a29_iterator(Graph_nodes obj1, Handle<Graph_nodes::Key0, Graph_nodes::Val0> cur, unsigned int arg) : obj1(obj1), cur(cur), arg(arg), reg4(arg) {
    get_record();
  }

  [[gnu::always_inline]] void get_record() {
    if (found_res)
      return;
    reg[2] = 3;
  mark_5:
    if ((cur.key().u >= reg2)) {
      goto mark_12;
    }
    group1 = obj1.search(  Graph_nodes::Key1{ .u = cur.key().u });
    comp_result = group1.value().color - reg4;
    if (comp_result < 0 || comp_result == 0) {
      goto mark_11;
    }
    res = { .color = group1.value().color };
    found_res = true;
    reg1--;
    if (reg1 == 0) {
      goto mark_12;
    }
  mark_11:
    cur = obj1.ngr(Graph_nodes::Key0{.index = Graph_nodes::idx_max, .u = cur.key().u});
    if ((bool) cur) {
      goto mark_5;
    }
  mark_12:
    terminated = true;
    return;
  }

  [[gnu::always_inline]] q_c346a6a29_record operator*() const {
    return res;
  }

  [[gnu::always_inline]] q_c346a6a29_iterator& operator++() {
    found_res = false;
    if (terminated) {
      return *this;
    }
    get_record();
    return *this;
  }

  [[gnu::always_inline]] bool operator==(const q_c346a6a29_iterator rhs) {
    assert(obj1.struct_number == rhs.obj1.struct_number);
    return ((((bool) cur == false) && ((bool) rhs.cur == false)) || (**this == *rhs));
  }

  [[gnu::always_inline]] bool operator==(const q_c346a6a29_sentinel rhs) {
    return ((found_res == false) && (((bool) cur == false) || (terminated)));
  }
};
struct q_c346a6a29_range {
  Graph_nodes obj0;
  unsigned int arg;
  [[gnu::always_inline]] q_c346a6a29_range(Graph_nodes obj0, unsigned int arg) : obj0(obj0), arg(arg) {}
  [[gnu::always_inline]] auto begin() {return q_c346a6a29_iterator(obj0, obj0.get_first(), arg);}
  [[gnu::always_inline]] auto end() {return q_c346a6a29_sentinel{};}
};
#endif
""",
),
(
"""
INSERT INTO graph_nodes(u, pu, eQ, du, color) VALUES
(:u, 1, 2, 3, 4),
(:u, :pu, :eQ, 5, 5);
""",
"""
void q_35b163ab0(Graph_nodes obj, unsigned int u, unsigned int pu, unsigned int eQ) {
  obj.ins_sync(Graph_nodes::Key0{.u=u}, Graph_nodes::Val0{.pu=1,.eQ=2});
  obj.ins_sync(Graph_nodes::Key1{.u=u}, Graph_nodes::Val1{.du=3,.color=4});
  obj.ins_sync(Graph_nodes::Key0{.u=u}, Graph_nodes::Val0{.pu=pu,.eQ=eQ});
  obj.ins_sync(Graph_nodes::Key1{.u=u}, Graph_nodes::Val1{.du=5,.color=5});
}
"""
)
])
def test_transform(code_generator, sql_statement: str, expected_code: str):
    transformed = code_generator.translate(sql_statement)[0]
    assert transformed.strip('\n') == expected_code.strip('\n')

def test_transform_regex(code_generator_fun):
    sql_statement = """
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
"""
    transformed = code_generator_fun.translate(sql_statement, 'gn')[0]
    match = re.search(r"constexpr Graph_nodes (.+)\(1\);", transformed)
    assert match.group(1) == "gn"

def test_transform_refname_skip(code_generator_fun):
    sql_statement = """
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
"""
    transformed = code_generator_fun.translate(sql_statement, '_')[0]
    match = re.search(r"constexpr Graph_nodes (.+)\(1\);", transformed)
    assert match.group(1) == "GRAPH_NODES"


@pytest.mark.parametrize('sql_statement, ref_names', [
(
"""
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
""", ['gn', 'gn2'])
])
def test_transform_refname_exception(code_generator_fun, sql_statement: str, ref_names: str | list[str]):
    with pytest.raises(ValueError):
        code_generator_fun.translate(sql_statement, ref_names)

@pytest.mark.parametrize('sql_statement, exception_message', [
    ('''
CREATE TABLE graph_nodes(
    u INT8 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );''',
    "Too many groups! Key has only 0 free bits, thus a maximum of -1 can be added to a primary group!"),
    ('''
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT9 NOT NULL,
    color INT3 NOT NULL
    );''',
    "Column 'du' is larger than `keyval_size` (9 > 8) and cannot be fitted in a group"),
    ('''
CREATE TABLE graph_nodes(
    u INT4 NOT NULL,
    pu INT5 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL,
    PRIMARY KEY (pu, u)
    );''',
    "In 'graph_nodes' group ['pu', 'u'] (PK) size is greater than keyval_size=8"),
    ('''SELECT * FROM table1, table2;''',
    "Currently only single-table queries are supported!"),
    ('''
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
    SELECT * FROM graph_nodes;''',
    "Return row size is limited and return row is greater than keyval size!"),
    ("""
INSERT INTO graph_nodes(u, pu, eQ, du, color) VALUES
(:u, 1, 2, 3, 4),
(:u, :pu, :eQ, 5, 5);
""", "Table graph_nodes not found"),
    ('''
CREATE TABLE graph_nodes(
    u INT4 PRIMARY KEY,
    pu INT4 NOT NULL,
    eQ BOOLEAN NOT NULL,
    du INT4 NOT NULL,
    color INT3 NOT NULL
    );
INSERT INTO graph_nodes(u, pu, eQ, du) VALUES
    (:u, 1, 2, 3),
    (:u, :pu, :eQ, 5);''',
    "Table columns do not match insert. Use all the column names in insert statement."),
])
def test_transform_exceptions(code_generator_fun, sql_statement, exception_message):
    with pytest.raises(RuntimeError) as e_info:
        code_generator_fun.translate(sql_statement)
    assert str(e_info.value) == exception_message
