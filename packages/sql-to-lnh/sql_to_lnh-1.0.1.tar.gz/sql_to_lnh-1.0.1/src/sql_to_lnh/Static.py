FILESTART = """
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
"""

FILEEND = """
#endif
"""
