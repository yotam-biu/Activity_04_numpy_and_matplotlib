import pytest
import numpy as np
from numpy.testing import assert_almost_equal
import matplotlib.pyplot as plt

from ..tst import import_file, _test_file

FILENAME = "problem3.py"

@pytest.fixture(scope="module")
def module():
    with plt.matplotlib.rc_context({'backend': 'Agg'}):
        yield import_file(FILENAME)  # runs code

def test_png(module, filename="sinc.png"):
    _test_file(filename)
    # just make sure we can load it as an image file, not sure
    # how to do a real image comparison...
    img = plt.imread(filename)
    assert len(img.shape) == 3

def test_axes(module):
    ax = plt.gca()

    assert ax.get_xlabel() == 'x', "Label of x-axis is not correct."
    assert ax.get_ylabel() == 'y = sinc(x)', "Label of y-axis is not correct."

    lines = ax.lines[0]
    x, y = lines.get_data()
    assert_almost_equal(x, np.linspace(-6, 6, 601),
                        err_msg="X values are not correct in plot")
    assert_almost_equal(y, np.sinc(np.linspace(-6, 6, 601)),
                        err_msg="Y values are not correct in plot")



