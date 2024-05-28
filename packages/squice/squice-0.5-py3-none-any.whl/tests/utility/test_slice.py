import sys
import os
import inspect
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent), ""))
sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent.parent), ""))
sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent.parent), "squice"))
sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent.parent.parent), ""))

print(sys.path)
from squice import DataLoaders as dl
from squice import MtxInterpolator as mi
from squice import GridMaker as gm
from squice import SpaceTransform as sp

from os.path import dirname, abspath
import sys

DIR = dirname(abspath(__file__))
print(DIR)


# ---------------------------------------------------------------------------
def test_slice():
    print(f"Testing utility: {inspect.stack()[0][3]}")
    # matrix data
    npf = dl.NumpyNow("[[[1,2], [3,4]], [[5,6], [7,8]]]")
    npf.load()

    # interpolator
    interp = mi.Linear(npf.mtx)

    # unit grid
    grid = gm.GridMaker()
    slice_grid = grid.get_unit_grid(2, 2)
    print(slice_grid)
    print(slice_grid.shape())

    # space transformer
    spc = sp.SpaceTransform("(0.5,0.5,0.5)", (0, 0.5, 0), (0.5, 0, 0))
    xyz_coords = spc.convert_coords(slice_grid)

    # get all vals from interpolator
    vals = interp.get_val_slice(xyz_coords)
    print(vals)
    print(vals[:, :, 0])


###########################################################################
if __name__ == "__main__":
    test_slice()
