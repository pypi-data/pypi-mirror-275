"""
Module to interpolate inside a numpy matrix with some bespoke methods
"""

from abc import ABC, abstractmethod
from DataLoaders import NumpyNow


####################################################################################
class MtxInterpolator(ABC):
    """Abstract class to define the methods for interpolation of a 3d numpy matrix"""

    def __init__(self, mtx):
        self.mtx = mtx

    @abstractmethod
    def get_value(self, x, y, z):
        pass


####################################################################################
class Nearest(MtxInterpolator):
    """
    This interpolator returns the nearest value closest to the point
    """

    def get_value(self, x, y, z):
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

        # print(x,y,z,self.mtx[x][y][z])
        # print(dimX,dimY,dimZ)

        return self.mtx[x][y][z]


####################################################################################

if __name__ == "__main__":
    npf = NumpyNow(
        "[[[1,2],[3,4],[3,4]], [[5,6],[7,8],[7,8]], [[5,6],[7,8],[7,8]], [[5,6],[7,8],[7,9]]]"
    )
    npf.load()
    nr = Nearest(npf.mtx)
    xx, yy, zz = npf.mtx.shape
    for x in range(xx):
        for y in range(yy):
            for z in range(zz):
                print(nr.get_value(x + 0.4, y + 0.4, z + 0.4))
                print(nr.get_value(x + 0.6, y + 0.6, z + 0.6))

    # print(nr.get_value(0,0,0))
    # print(nr.get_value(0.5,0.5,5.5))
    # print(nr.get_value(3,2,1))
