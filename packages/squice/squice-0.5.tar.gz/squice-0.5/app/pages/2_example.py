import streamlit as st
from squice import DataLoaders as dl
from squice import VectorThree as v3
from squice import MtxInterpolator as mi
from squice import GridMaker as gm
from squice import SpaceTransform as sp
import plotly.graph_objs as go
import io
import numpy as np
import os
import uuid

st.set_page_config(
    page_title="squice",
    page_icon="app/static/squice.png",
    layout="wide",
)

st.title("SQUICE: Example")

MY_MTX = None

tabData, tabAll, tabSlice, tabWedge = st.tabs(["data", "matrix", "slice", "chunk"])
with tabData:

    option = st.radio(
        "Data loaded from:",
        ["Manual", "NumpyFile", "Electron Density", "Electron Microscopy", "PDB/CIF"],
        horizontal=True,
    )
    if option == "Manual":
        mtx_txt = """[[[0,0,0],[0,3,0],[0,0,0]],
        [[0,0,0],[3,5,0],[0,0,0]],
        [[0,0,0],[0,0,1],[0,0,0]]]
        """
        data_str = st.text_area("Matrix", mtx_txt, height=200).strip()
        MY_MTX = dl.NumpyNow(data_str)
        MY_MTX.load()
    elif option == "NumpyFile":
        uploaded_file = st.file_uploader(
            "Upload numpy file", type="npy", accept_multiple_files=False
        )
        if uploaded_file is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getbuffer()
            filename = str(uuid.uuid4())
            with open(filename, "wb") as wb:
                wb.write(bytes_data)
            MY_MTX = dl.NumpyFile(filename)
            MY_MTX.load()
            if os.path.exists(filename):
                os.remove(filename)
            mtx_str = str(MY_MTX.mtx)

            # mtx_str = mtx_str.replace("\n"," ")
            # mtx_str = mtx_str.replace("\t"," ")
            while mtx_str.count("  ") > 0:
                mtx_str = mtx_str.replace("  ", " ")
            mtx_str = mtx_str.replace("]", "],")
            mtx_str = mtx_str.replace(",]", "]")
            mtx_str = mtx_str.replace(" [", "[")
            mtx_str = mtx_str.replace(" ", ",")
            mtx_str = mtx_str.replace(",]", "]")
            mtx_str = mtx_str.replace("]]],", "]]]")
            data_str = st.text_area("Matrix", mtx_str, height=200).strip()
            MY_MTX = dl.NumpyNow(data_str)
            MY_MTX.load()

    else:
        st.error("Apologies, only numpy data is currently implemented")

    # some display and save of data
    if MY_MTX is not None:

        # display the data
        cols = st.columns(3)
        with cols[0]:
            with st.popover("Show mtx data"):
                st.write(MY_MTX.mtx)

        filename = "matrix.npy"
        with cols[1]:
            filename = st.text_input("fname", filename, label_visibility="collapsed")
        with cols[2]:
            # save the data with an in-memory buffer
            with io.BytesIO() as buffer:
                # Write array to buffer
                np.save(buffer, MY_MTX.mtx)
                btn = st.download_button(
                    label="Download mtx",
                    data=buffer,  # Download buffer
                    file_name=filename,
                )
if MY_MTX is not None:

    with tabAll:
        st.write("### Raw matrix data")

        xs = []
        ys = []
        zs = []
        values = []
        minv = None
        maxv = None

        a, b, c = MY_MTX.mtx.shape
        for i in range(a):
            for j in range(b):
                for k in range(a):
                    val = 0
                    if k < c:
                        val = MY_MTX.mtx[i][j][k]
                        if minv is None:
                            minv = val
                            maxv = val
                        else:
                            minv = min(minv, val)
                            maxv = max(maxv, val)
                    xs.append(i)
                    ys.append(j)
                    zs.append(k)
                    values.append(val)

        c0 = "rgba(119,136,153,1)"
        c1 = "rgba(240,248,255,0)"
        c2 = "rgba(100,149,237,0.5)"
        c3 = "rgba(220,20,60,0.9)"
        c4 = "rgba(100,0,0,1)"

        zero = 1 - (maxv / abs(maxv - minv))
        zer0 = max(0.01, zero)
        zer1 = max(zer0 * 1.5, 0.5)
        zer2 = max(zer0 * 1.9, 0.8)

        colorscale = [(0, c0), (zer0, c1), (zer1, c2), (zer2, c3), (1, c4)]

        fig = go.Figure(
            data=go.Isosurface(
                x=xs,
                y=ys,
                z=zs,
                value=values,
                colorscale=colorscale,
                showscale=True,
                showlegend=False,
                opacity=0.6,
                surface_count=20,
                caps=dict(x_show=False, y_show=False),
                isomin=minv,
                isomax=maxv,
            )
        )

        fig.update_xaxes(showticklabels=False, visible=False)  # hide all the xticks
        fig.update_yaxes(showticklabels=False, visible=False)  # hide all the xticks
        fig.update_yaxes(scaleanchor="x", scaleratio=1)
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        # Plot!
        st.plotly_chart(fig, use_container_width=True)

    with tabSlice:
        st.write("### Slice through the matrix")
        st.caption(
            """To define a slice through an orthogonal grid,
        we need to have 3 points to define a plane. These we will define as the points that are:
        - central - linear  - planar
        Additionally we need to know:
        - width of the slice
        - sample frequency
        The width can be considered the zoom; the sample frequence, the resolution.
        """
        )
        "---"
        xx, yy, zz = MY_MTX.mtx.shape
        if "central" in st.session_state:
            central = st.session_state["central"]
            print(central)
        else:
            central = f"({xx/2}, {yy/2}, 0)"
            st.session_state["central"] = central

        if "linear" in st.session_state:
            linear = st.session_state["linear"]
        else:
            linear = f"({xx}, {yy/2}, 0)"
            st.session_state["linear"] = linear

        if "planar" in st.session_state:
            planar = st.session_state["planar"]
        else:
            planar = f"({xx/2}, {yy}, 0)"
            st.session_state["planar"] = planar

        cols = st.columns(3)
        with cols[0]:
            interper = st.radio("Interpolator", ["Nearest", "Linear"], index=1)
        with cols[1]:
            width = st.slider(
                "Width", 0, 2 * max(MY_MTX.mtx.shape), value=min(MY_MTX.mtx.shape)
            )
            samples = st.slider("Samples", 0, 50, value=10)
        with cols[2]:
            st.caption("Enter points in the format (0,1, 1.2, 3.4)")
            params = {}
            params.setdefault("label_visibility", "collapsed")
            c1, c2 = st.columns([2, 5])
            c1.markdown("central: :red[*]")
            central = c2.text_input("", central, **params)
            c1, c2 = st.columns([2, 5])
            c1.markdown("linear: :red[*]")
            linear = c2.text_input("", linear, **params)
            c1, c2 = st.columns([2, 5])
            c1.markdown("planar: :red[*]")
            planar = c2.text_input("", planar, **params)

        # interpolator
        if interper == "Linear":
            interp = mi.Linear(MY_MTX.mtx)
        else:
            interp = mi.Nearest(MY_MTX.mtx)

        # unit grid
        grid = gm.GridMaker()
        slice_grid = grid.get_unit_grid(width, samples)

        # space transformer
        spc = sp.SpaceTransform(central, linear, planar)
        xyz_coords = spc.convert_coords(slice_grid)

        # get all vals from interpolator
        vals = interp.get_val_slice(xyz_coords)[:, :, 0]
        xx, yy = vals.shape

        x = list(range(0, xx))
        y = list(range(0, yy))

        if st.button("rotate"):
            vcentral = spc.navigate(v3.VectorThree(abc=central), "CL", 0.01)
            vlinear = spc.navigate(v3.VectorThree(abc=linear), "CL", 0.01)
            vplanar = spc.navigate(v3.VectorThree(abc=planar), "CL", 0.01)
            st.session_state["central"] = vcentral.to_coords_str()
            st.session_state["linear"] = vlinear.to_coords_str()
            st.session_state["planar"] = vplanar.to_coords_str()

        fig = go.Figure(
            data=go.Heatmap(
                z=vals,
                x=x,
                y=y,
                colorscale=[
                    (0, "aliceblue"),
                    (0.2, "cornflowerblue"),
                    (0.9, "crimson"),
                    (1.0, "rgb(100,0,0)"),
                ],
                showscale=True,
            )
        )

        fig.update_xaxes(showticklabels=True, visible=False)  # hide all the xticks
        fig.update_yaxes(showticklabels=True, visible=False)  # hide all the xticks
        fig.update_yaxes(scaleanchor="x", scaleratio=1)
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        # Plot!
        st.plotly_chart(fig, use_container_width=True)
