import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

FILENAME = "problem2.py"


@pytest.fixture(scope="module")
def translate():
    return get_attribute("translate", FILENAME)

@pytest.mark.parametrize("x,t",
                         [
                             (np.array(
                                 [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0],
                                  [1.34234, 0.0,  1.34234], [0.0, 1.34234, 1.34234]]),
                              np.array([1.34234, -1.34234, -1.34234])),
                             (np.array([[1.5, -1.5, 3], [-1.5, -1.5, -3]]),
                              np.array([-1.5, 1.5, 3]))
                         ])
def test_translate_function(translate, x, t):
    assert_almost_equal(translate(x, t), x + t)

