# SQL to LNH

Проект предназначен для конвертацию выражений SQL в выражения языка C++, совместимые с библиотекой LNH L0.

## Цели проекта

Основной целью является создание более высокоуровневого инструмент для описания структур LNH и методов их обработки, чем код на C.

## Возможности в текущей версии

- Парсинг SQL выражений `CREATE TABLE`:
  - Ключ можно задать с использованием ключевых слов `PRIMARY KEY` при описании столбца или выражения `PRIMARY KEY (col1, col2)` при описании всей таблицы
  - Поддерживаются поля типов `INT{N}`, `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `INTEGER`, `BIGINTEGER`, а также `BOOLEAN`. Размеры полей возможно задать только в байтах
- Преобразование выражений `CREATE TABLE` в шаблонный код на C:
  - Размер поля определяется параметром `keyval_size`
  - Имеется поддержка расширения структуры путём частичного дублирования ключа, как в [btwc-dijkstra-xrt](https://gitlab.com/leonhard-x64-xrt-v2/btwc-example/btwc-dijkstra-xrt/-/blob/iterators/sw-kernel/include/graph_iterators.hxx)
  - Значения группируются "наивным" алгоритмом: выбираются в порядке их объявления, и если места в группе для значения не хватает, то формируется новая группа, в которую помещается новое значение
- Задание алгоритмов поиска данных и обхода структур через выражения `SELECT`
  - Поддерживается поиск только по одной таблице
  - Поддерживаются псевдонимы таблиц и столбцов, `LIMIT`, `ORDER BY`, `WHERE`
  - Поддерживаются поименованные параметры подстановки типа `:foo, $bar`
  - Поддержка функций агрегации не подтверждена
- Создание функций вставки из выражений `INSERT INTO`
  - Необходимо перечислить все столбцы для вставки

## Установка

Установить можно с помощью команды:

```
pip install sql_to_lnh
```

## Использование

### CLI

С пакетом предоставляется CLI-утилита для тестирования. Запустите в терминале командой `sql_to_lnh`. На вход предоставляется
выражение SQL, имя объекта, на выходе генерируется необходимый фрагмент C++ кода. Пример:

```
Введите SQL-выражение
>>> CREATE TABLE users(
>>>  idx     INT4 NOT NULL,
>>>  user    INT4 NOT NULL,
>>>  role    INT4 NOT NULL,
>>>  time    INT4 NOT NULL,
>>>  PRIMARY KEY (idx, user)
>>>  )
>>>
Имя объекта (Enter для имени по-умолчанию):
USERS
Результат трансляции:
struct Users {
  int struct_number;
  constexpr Users(int struct_number) : struct_number(struct_number) {}
  STRUCT(Key0) {
    unsigned int idx: 32;
    unsigned int user: 32;
  };
  STRUCT(Val0) {
    unsigned int role: 32;
    unsigned int time: 32;
  };
  #ifdef __riscv64__
  DEFINE_DEFAULT_KEYVAL(Key0, Val0)
  #endif
};

constexpr Users USERS(1);

Введите SQL-выражение
>>>
```

### cog

С пакетом распространяется утилита для кодогенерации cog. Cog позволяет включать в файлы с исходным кодом комментарии,
которые содержат код на python, исполнять код из комментариев и результат работы печатать в исходный файл.

Чтобы создать модуль с объявлениями, который можно использовать в проекте для LNH, создайте файл с комментариями для cog
(к примеру, `codegen.h`). В комментариях cog необходимо:

1. Инициализировать модуль:

```cpp
/*[[[cog
from sql_to_lnh.CogPrinter import CogPrinter

codegen = CogPrinter('sql_to_lnh.db')
]]]*/
//[[[end]]]
```

2. Вызвать модуль кодогенерации с выражением SQL и именем структуры (опционально):

```cpp
/*[[[cog
users_SQL = """
CREATE TABLE users(
  idx		    INT4 NOT NULL,
  user       INT4 NOT NULL,
  role       INT4 NOT NULL,
  time    INT4 NOT NULL,
  PRIMARY KEY (idx, user)
  )"""
codegen.translate(users_SQL, 'USERS')
]]]*/
//[[[end]]]
```

3. Закрыть модуль кодогенерации:

```cpp
/*[[[cog
codegen.close()
]]]*/
//[[[end]]]
```

4. Вызвать cog командой `cog -r [ИМЯ ФАЙЛА]`. В результате будет получен файл:

```cpp
/*[[[cog
from sql_to_lnh.CogPrinter import CogPrinter

codegen = CogPrinter('sql_to_lnh.db')
]]]*/

#ifndef GITERS_H_
#define GITERS_H_


#include <stdlib.h>
#include <stdint.h>
#include <cmath>
#include <cassert>
#ifdef __riscv64__
#include "map.h"
#endif
#include "compose_keys.hxx"

#define DEBUG

#ifdef __riscv64__
template<typename K, typename V>
struct Handle {
        bool ret_val;
        K k{get_result_key<K>()};
        V v{get_result_value<V>()};
        [[gnu::always_inline]] Handle(bool ret_val) : ret_val(ret_val) {
        }

        [[gnu::always_inline]] operator bool() const {
                return ret_val;
        }

        [[gnu::always_inline]] K key() const {
                return k;
        }

        [[gnu::always_inline]] V value() const {
                return v;
        }
};
#endif

//[[[end]]]

/*[[[cog
users_SQL = """
CREATE TABLE users(
  idx		    INT4 NOT NULL,
  user       INT4 NOT NULL,
  role       INT4 NOT NULL,
  time    INT4 NOT NULL,
  PRIMARY KEY (idx, user)
  )"""
codegen.translate(users_SQL, 'USERS')
]]]*/
struct Users {
  int struct_number;
  constexpr Users(int struct_number) : struct_number(struct_number) {}
  STRUCT(Key0) {
    unsigned int idx: 32;
    unsigned int user: 32;
  };
  STRUCT(Val0) {
    unsigned int role: 32;
    unsigned int time: 32;
  };
  #ifdef __riscv64__
  DEFINE_DEFAULT_KEYVAL(Key0, Val0)
  #endif
};

constexpr Users USERS(1);

//[[[end]]]

/*[[[cog
codegen.close()
]]]*/

#endif

//[[[end]]]
```
