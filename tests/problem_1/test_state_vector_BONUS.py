import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem1.py"

def test_sy_expectation_value():
    value = get_attribute("result1d", FILENAME)
    sy = get_attribute("sy", FILENAME)
    v = 1/np.sqrt(2) * np.array([1, -1j])
    ref = v.conjugate().T.dot(sy.dot(v))
    assert_almost_equal(value, ref)

