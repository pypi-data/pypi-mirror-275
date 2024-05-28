"""
Module to interpolate inside a numpy matrix with some bespoke methods
"""

from abc import ABC, abstractmethod
from .DataLoaders import NumpyNow
from scipy.interpolate import RegularGridInterpolator
import numpy as np
import math


####################################################################################
class MtxInterpolator(ABC):
    """
    Abstract class to define the methods for interpolation of a 3d numpy matrix.
    There are 3 methods of wrapping the data if it is out of bounds:
    - cap : it is simply fixed at the bounds if it goes beyond
    - periodic: it loops to make it a periodic shape eg 3.1 becomes 0.1 if the max is 3
    - mirror: the edges reflect back, best only with small bleeds in the edge


    """

    def __init__(self, mtx, wrap="none"):
        self.mtx = mtx
        self.wrap = wrap

    def get_value(self, x, y, z):
        # 1. first validate inputs
        xx, yy, zz = self.mtx.shape
        if self.wrap == "periodic":
            x = (math.floor(x) // xx) + (x - math.floor(x))
            y = (math.floor(y) // yy) + (y - math.floor(y))
            z = (math.floor(z) // zz) + (z - math.floor(z))
        elif self.wrap == "mirror":
            if x - xx - 1 > 0:
                x = xx - (x - xx)
            x = (math.floor(x) // xx) + (x - math.floor(x))
            y = (math.floor(y) // yy) + (y - math.floor(y))
            z = (math.floor(z) // zz) + (z - math.floor(z))
        elif self.wrap == "cap":
            x = min(x, xx - 1)
            y = min(y, yy - 1)
            z = min(z, zz - 1)
            x = max(x, 0)
            y = max(y, 0)
            z = max(z, 0)
        else:
            x, y, z = round(x, 4), round(y, 4), round(z, 4)
            if x > xx - 1 or y > yy - 1 or z > zz - 1:
                return None
            if x < 0 or y < 0 or z < 0:
                return None

        # 2. get the value from the interpolator
        return self._get_value(x, y, z)

    @abstractmethod
    def _get_value(self, x, y, z):
        pass

    def get_val_slice(self, coords_mtx):
        """
        A matrix of coordinates for creating values.
        The matrix is a custom 3d format called Matrix3d.
        """

        ret_mtx = np.zeros(coords_mtx.shape())
        a, b, c = ret_mtx.shape
        for i in range(a):
            for j in range(b):
                for k in range(c):
                    coord = coords_mtx.get(i, j, k)
                    z = self.get_value(coord.A, coord.B, coord.C)
                    ret_mtx[i][j][k] = z
        return ret_mtx


####################################################################################
class Nearest(MtxInterpolator):
    """
    This interpolator returns the nearest value closest to the point
    """

    def _get_value(self, x, y, z):
        """Given a position return the interpolated value"""
        dimX, dimY, dimZ = self.mtx.shape
        x = int(round(x, 0))
        y = int(round(y, 0))
        z = int(round(z, 0))
        x = max(x, 0)
        y = max(y, 0)
        z = max(z, 0)
        x = min(x, dimX - 1)
        y = min(y, dimY - 1)
        z = min(z, dimZ - 1)
        return self.mtx[x][y][z]


####################################################################################
class Linear(MtxInterpolator):
    """
    This interpolator returns a linear interpolation of the point
    """

    def _get_value(self, x, y, z):
        xx, yy, zz = self.mtx.shape
        fit_points = [
            np.linspace(0, xx - 1, xx),
            np.linspace(0, yy - 1, yy),
            np.linspace(0, zz - 1, zz),
        ]
        fni = RegularGridInterpolator(fit_points, self.mtx)
        pts = np.array([[x, y, z]])
        z = fni(pts)[0]
        return z


####################################################################################

if __name__ == "__main__":
    npf = NumpyNow(
        "[[[1,2],[3,4],[3,4]], [[5,6],[7,8],[7,8]], [[5,6],[7,8],[7,8]], [[5,6],[7,8],[7,9]]]"
    )
    npf.load()
    interps = []
    interps.append(Nearest(npf.mtx))
    interps.append(Linear(npf.mtx))

    for interp in interps:
        xx, yy, zz = npf.mtx.shape
        for x in range(xx):
            for y in range(yy):
                for z in range(zz):
                    print(interp.get_value(x + 0.4, y + 0.4, z + 0.4))
                    print(interp.get_value(x + 0.6, y + 0.6, z + 0.6))

    # print(nr.get_value(0,0,0))
    # print(nr.get_value(0.5,0.5,5.5))
    # print(nr.get_value(3,2,1))
