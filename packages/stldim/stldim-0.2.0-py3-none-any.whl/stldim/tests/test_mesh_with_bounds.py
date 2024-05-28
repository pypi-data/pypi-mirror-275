"""
Test the MeshWithBounds class
"""

import pytest
import stldim

def test_3dbenchy():
    """
    Calculate the dimmensions of the 3DBenchy model and compare them to known values.
    """
    stl_dimensions = stldim.MeshWithBounds.from_file("tests/3DBenchy.stl")

    assert pytest.approx(stl_dimensions['minx']) == -29.176
    assert pytest.approx(stl_dimensions['maxx']) == 30.825
    assert pytest.approx(stl_dimensions['miny']) == -15.502
    assert pytest.approx(stl_dimensions['maxy']) == 15.502
    assert pytest.approx(stl_dimensions['minz']) == 0.0
    assert pytest.approx(stl_dimensions['maxz']) == 48.0
