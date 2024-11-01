# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 04 (numpy and matplotlib)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 1

def test_second_particle_coordinates():
    return _test_variable("result2c", [1.34234, 1.34234, 0.0],
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
