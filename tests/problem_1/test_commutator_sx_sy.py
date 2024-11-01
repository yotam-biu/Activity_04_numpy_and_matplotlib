import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem1.py"

def test_commutator():
    value = get_attribute("result1c", FILENAME)
    sz = get_attribute("sz", FILENAME)
    assert_almost_equal(value, 2*1j*sz)

