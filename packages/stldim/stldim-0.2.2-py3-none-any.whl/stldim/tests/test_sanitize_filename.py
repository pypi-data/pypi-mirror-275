"""
Tests for the sanitize_filename function in the stldim module.
"""

import stldim

def test_plain():
    """
    Test with a plain filename
    """
    print(dir(stldim))
    assert stldim.sanitize_filename("test.stl") == "test_stl"

def test_spaces():
    """
    Test with spaces in the filename
    """
    assert stldim.sanitize_filename("test test.stl") == "test_test_stl"

def test_special_chars():
    """
    Test with special characters in the filename
    """
    assert stldim.sanitize_filename("test!@#$%^&*().stl") == "test___________stl"

def test_leading_numbers():
    """
    Test with leading numbers in the filename
    """
    assert stldim.sanitize_filename("11test.stl") == "__test_stl"

def test_trailing_numbers():
    """
    Test with trailing numbers in the filename
    """
    assert stldim.sanitize_filename("test11.stl") == "test11_stl"

def test_no_extension():
    """
    Test with a filename with no extension
    """
    assert stldim.sanitize_filename("test") == "test"

def test_subdirectory():
    """
    Test with a filename with a subdirectory
    """
    assert stldim.sanitize_filename("subdir/test.stl") == "test_stl"
