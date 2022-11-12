"""
The conftest.py file serves as a means of
providing fixtures for an entire directory.
"""

import os
import sys
import pytest

GMDH_ROOT = os.environ['GMDH_ROOT']
sys.path.append(GMDH_ROOT)

import gmdh  # pylint: disable=wrong-import-position

@pytest.fixture(autouse=True)
def add_gmdhpy(doctest_namespace):
    """
    Injecting `gmdh` module name into
    the namespace in which doctests run.
    """
    doctest_namespace["gmdh"] = gmdh
