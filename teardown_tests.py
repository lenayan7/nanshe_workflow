#!/usr/bin/env python


import os
import shutil
import sys


if not os.environ.get("TEST_NOTEBOOKS"):
    sys.exit(0)

for each in list(sys.argv[1:]) + [
    "data.tif",
    "data.h5",
    "data_trim.h5",
    "data_dn.h5",
    "data_reg.h5",
    "data_sub.h5",
    "data_f_f0.h5",
    "data_wt.h5",
    "data_norm.h5",
    "data_dict.h5",
    "data_post.h5",
    "data_traces.h5",
    "data_rois.h5",
    "data_proj.h5",
    "data.zarr",
    "data_trim.zarr",
    "data_dn.zarr",
    "data_reg.zarr",
    "data_sub.zarr",
    "data_f_f0.zarr",
    "data_wt.zarr",
    "data_norm.zarr",
    "data_dict.zarr",
    "data_post.zarr",
    "data_traces.zarr",
    "data_rois.zarr",
    "data_proj.zarr",
    "data_proj.html"]:
    if os.path.isfile(each):
        os.remove(each)
    elif os.path.isdir(each):
        shutil.rmtree(each)
