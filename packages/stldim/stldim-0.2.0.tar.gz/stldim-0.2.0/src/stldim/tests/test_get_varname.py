"""
Test the get_varname function
"""

import stldim

def test_empty_varname():
    """
    Test with an empty varnames
    """
    assert stldim.get_varname("test.stl", "") == "test_stl"

def test_none_varname():
    """
    Test with varname set to None
    """
    assert stldim.get_varname("test.stl", None) == "test_stl"

def test_varname():
    """
    Test with a varname set
    """
    assert stldim.get_varname("test.stl", "foobar") == "foobar"
