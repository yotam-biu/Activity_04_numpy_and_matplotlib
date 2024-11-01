# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 04 (numpy and matplotlib)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 3

def test_translate_particles():
    return _test_variable("result2f", [[ 1.34234, -1.34234, -1.34234],
 [ 2.68468,  0.     , -1.34234],
 [ 2.68468, -1.34234,  0.     ],
 [ 1.34234,  0.     ,  0.     ]]
,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )