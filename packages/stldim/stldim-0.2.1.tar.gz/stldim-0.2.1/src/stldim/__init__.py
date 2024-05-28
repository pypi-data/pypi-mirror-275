"""
A module that provides a class that extends the stl.Mesh class to include properties for the mesh's
dimensions.
"""

import os
import re

import stl
from stl import mesh


class MeshWithBounds(mesh.Mesh):
    """
    A class that extends the stl.Mesh class to include properties for the mesh's dimensions.
    """

    @property
    def maxx(self):
        """Calculate and return the maximum x of the mesh."""
        return max(self.points, key=lambda p: p[stl.Dimension.X.value])[stl.Dimension.X.value]

    @property
    def minx(self):
        """Calculate and return the minimum x of the mesh."""
        return min(self.points, key=lambda p: p[stl.Dimension.X.value])[stl.Dimension.X.value]

    @property
    def maxy(self):
        """Calculate and return the maximum y of the mesh."""
        return max(self.points, key=lambda p: p[stl.Dimension.Y.value])[stl.Dimension.Y.value]

    @property
    def miny(self):
        """Calculate and return the minimum y of the mesh."""
        return min(self.points, key=lambda p: p[stl.Dimension.Y.value])[stl.Dimension.Y.value]

    @property
    def maxz(self):
        """Calculate and return the maximum z of the mesh."""
        return max(self.points, key=lambda p: p[stl.Dimension.Z.value])[stl.Dimension.Z.value]

    @property
    def minz(self):
        """Calculate and return the minimum z of the mesh."""
        return min(self.points, key=lambda p: p[stl.Dimension.Z.value])[stl.Dimension.Z.value]

    @property
    def xsize(self):
        """Calculate and return the size of the mesh in the x direction."""
        return round(self.maxx - self.minx, 3)

    @property
    def ysize(self):
        """Calculate and return the size of the mesh in the y direction."""
        return round(self.maxy - self.miny, 3)

    @property
    def zsize(self):
        """Calculate and return the size of the mesh in the z direction."""
        return round(self.maxz - self.minz, 3)

    @property
    def midx(self):
        """Calculate and return the midpoint of the mesh in the x direction."""
        return round(self.xsize / 2, 3)

    @property
    def midy(self):
        """Calculate and return the midpoint of the mesh in the y direction."""
        return round(self.ysize / 2, 3)

    @property
    def midz(self):
        """Calculate and return the midpoint of the mesh in the z direction."""
        return round(self.zsize / 2, 3)

    @property
    def dimensions(self):
        """Return a dictionary of the mesh's dimensions."""
        return {
            'min_x': round(self.minx, 3),
            'max_x': round(self.maxx, 3),
            'min_y': round(self.miny, 3),
            'max_y': round(self.maxy, 3),
            'min_z': round(self.minz, 3),
            'max_z': round(self.maxz, 3),
            'x_size': round(self.xsize, 3),
            'y_size': round(self.ysize, 3),
            'z_size': round(self.zsize, 3),
            'mid_x': round(self.midx, 3),
            'mid_y': round(self.midy, 3),
            'mid_z': round(self.midz, 3),
        }

    def __getitem__(self, key):
        """
        Allow the object to be accessed like a dictionary.
        """
        return getattr(self, key)

def sanitize_filename(stlfile):
    """
    Replace every non-alphanumeric character with an underscore
    """

    sanitized = re.sub(r'\W', '_', os.path.basename(stlfile)).lower()
    match = re.search(r"\D", sanitized)
    if match:
        return "_" * (match.start()) + sanitized[match.start():]
    return sanitized


def get_varname(filename, name):
    """
    Return a sanitized variable name based on the filename and the provided name.
    """
    if name:
        return name
    return sanitize_filename(filename)
