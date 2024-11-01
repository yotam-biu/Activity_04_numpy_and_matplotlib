# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 04 (numpy and matplotlib)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 1

def test_second_particle_y_coordinate():
    return _test_variable("result2d", 1.34234,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
