# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 04 (numpy and matplotlib)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 1

def test_t_shape():
    return _test_variable("result2b_shape", (3, ),
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
