import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem1.py"

def test_product_sx_sy_sz():
    value = get_attribute("result1a", FILENAME)
    assert_almost_equal(value, np.zeros((2, 2), dtype=np.complex128))

