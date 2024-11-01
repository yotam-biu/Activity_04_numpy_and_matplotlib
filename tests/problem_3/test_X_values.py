import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem3.py"

def test_x_values():
    value = get_attribute("X", FILENAME)
    assert_almost_equal(value, np.linspace(-6, 6, 601))

