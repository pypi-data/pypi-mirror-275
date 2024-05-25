__author__ = "Paco Lopez Dekker"
__email__ = "F.LopezDekker@tudeft.nl"

import math
import os
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np
import numpy.ma as ma
import numpy.typing as npt
import scipy.io as spio
import xarray as xr
from drama import constants as cnst
from drama import utils as drtls
from matplotlib import pyplot as plt
from scipy import ndimage
from scipy.interpolate import griddata


def haversine(
    lon1: npt.ArrayLike, lat1: npt.ArrayLike, lon2: npt.ArrayLike, lat2: npt.ArrayLike
) -> npt.ArrayLike:
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    Parameters
    ----------
    lon1 : npt.ArrayLike
        Longitude(s) of the first point(s).
    lat1 : npt.ArrayLike
        Latitude(s) of the first point(s).
    lon2 : npt.ArrayLike
        Longitude(s) of the second point(s).
    lat2 : npt.ArrayLike
        Latitude(s) of the second point(s).

    Returns
    -------
    npt.ArrayLike
        The great circle distance(s) between each pair of points in
        the input. The distance(s) are measured in the same units as
        the radius of the Earth.
    """
    lon1, lat1, lon2, lat2 = map(np.deg2rad, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    distance = cnst.r_earth * c
    return distance


def calculate_resampled_locations(
    data_shape: Tuple, smp_in_x: float, smp_in_y: float, smp_out: float
) -> Tuple[npt.NDArray, npt.NDArray]:
    """
    Calculate resampled locations for a given input shape and desired sampling period.

    Parameters
    ----------
    data_shape : Tuple[int, int]
        Shape of the input data as (height, width).
    smp_in_x : float
        Sampling period along the x-axis.
    smp_in_y : float
        Sampling period along the y-axis.
    smp_out : float
        Sampling period of the output.

    Returns
    -------
    Tuple[npt.NDArray, npt.NDArray]
        Arrays containing the resampled x and y locations.

    Notes
    -----
    This function calculates resampled locations based on the input shape and
    sampling periods along the x and y axes. The resampled locations are evenly
    spaced according to the specified output sampling period.
    """
    nxo = int(np.floor(data_shape[1] * smp_in_x / smp_out))
    nyo = int(np.floor(data_shape[0] * smp_in_y / smp_out))
    xo = np.arange(nxo) * smp_out / smp_in_x
    yo = np.arange(nyo) * smp_out / smp_in_y
    return xo, yo


def _resample_model_data(
    observable: npt.NDArray, x_out: npt.NDArray, y_out: npt.NDArray
) -> npt.NDArray:
    """
    Linearly resample the observable using dramas resampling function.
    This is an internal function meant to be used when reading model
    inputs.

    Parameters
    ----------

    observable: npt.NDArray
        The data to resample.
    x_out: npt.NDArray
        The locations along the x-axis on which to resample to.
    y_out: npt.NDArray
        The locations along the y-axis on which to resample to.

    Returns
    -------
    npt.NDArray
        The resampled data.
    """
    return drtls.linresample(
        drtls.linresample(observable, x_out, axis=1, extrapolate=True),
        y_out,
        axis=0,
        extrapolate=True,
    )


def read_scenario_ifremer(
    ncfiles: Tuple[Path, Path, Path],
    smp_out: Optional[float] = None,
    rot_angle: Optional[float] = 0,
) -> tuple[Dict[str, npt.NDArray], float]:
    """Read the inputs from the Ifremer scene on the west coast of
    France, clean them and return a dictionary variables in the form
    that the workbench expects.

    Parameters
    ----------
    ncfiles : tuple of Path
        File path(s) to the Ifremer scene NetCDF file(s). The first
        entry of the tuple should be the path to the file with the
        outpus of the MARC forecasting system, which contains the
        sea-surface height anomaly. The second entry should be the
        outputs from the AROME model, containing the sea-surface
        temperature. The final entry should be the file containing the
        outputs of WaveWatch III.

    smp_out : float
        The desired spatial sampling period of the output.

    rot_angle : float
        Rotation angle in degrees.

    Returns
    -------
    tuple[Dict[str, npt.NDArray], float]
        A dictionary containing cleaned input variables in the format
        expected by the workbench and the spatial sampling period of
        the output.
    """
    marc_ds, arome_ds, ww3_ds = map(xr.open_dataset, ncfiles)
    # Use the SSHA grid as the reference
    lon, lat = marc_ds.longitude, marc_ds.latitude
    time = np.datetime64("2022-05-22T05:00:00.00")
    ssha_da = marc_ds.DELTA_XE.sel(time=time)
    ssha = ssha_da.to_numpy()
    # The MARC dataset has the NaN values over cells that correspond
    # to land. Use that as a mask for the WW3 dataset.
    ocean_mask = ~np.isnan(ssha)
    hs = ww3_ds.hs.sel(time=time)
    hs_mask = hs > 0
    tsc_v_component = ww3_ds.vcur.sel(time=time).where(hs_mask).to_numpy()
    tsc_u_component = ww3_ds.ucur.sel(time=time).where(hs_mask).to_numpy()
    lon_ww3 = ww3_ds.longitude.to_numpy()
    lat_ww3 = ww3_ds.latitude.to_numpy()
    tsc_v_component = griddata(
        (lon_ww3, lat_ww3), tsc_v_component, (lon, lat), method="linear"
    )
    tsc_u_component = griddata(
        (lon_ww3, lat_ww3), tsc_u_component, (lon, lat), method="linear"
    )
    tsc_v = np.zeros(tsc_v_component.shape + (2,))
    tsc_v[..., 0] = np.where(ocean_mask, tsc_u_component, np.nan)
    tsc_v[..., 1] = np.where(ocean_mask, tsc_v_component, np.nan)
    wind_v = np.zeros_like(tsc_v)
    wind_u_component = ww3_ds.uwnd.sel(time=time).where(hs_mask).to_numpy()
    wind_v_component = ww3_ds.vwnd.sel(time=time).where(hs_mask).to_numpy()
    wind_u_component = griddata(
        (lon_ww3, lat_ww3), wind_u_component, (lon, lat), method="linear"
    )
    wind_v_component = griddata(
        (lon_ww3, lat_ww3), wind_v_component, (lon, lat), method="linear"
    )
    wind_v[..., 0] = np.where(ocean_mask, wind_u_component, np.nan)
    wind_v[..., 1] = np.where(ocean_mask, wind_v_component, np.nan)
    sst = (
        arome_ds.t2m.sel(time=time, height=0)
        .interp(longitude=lon, latitude=lat)
        .to_numpy()
    )
    lon = lon.to_numpy()
    lat = lat.to_numpy()
    # Calculate the azimuth sampling from the lat-lon grid.
    dx = haversine(lon[0, 0], lat[0, 0], lon[0, 1], lat[0, 1])
    dy = haversine(lon[0, 0], lat[0, 0], lon[1, 0], lat[1, 0])
    if smp_out is None:
        smp_out = dx
    else:
        # Resample.
        xo, yo = calculate_resampled_locations(tsc_v.shape, dx, dy, smp_out)
        wind_v, tsc_v, sst, ssha, lon, lat = map(
            lambda data: _resample_model_data(data, xo, yo),
            (wind_v, tsc_v, sst, ssha, lon, lat),
        )

    if not math.isclose(rot_angle, 0):
        tsc_v = np.nan_to_num(tsc_v)
        wind_v = np.nan_to_num(wind_v)
        sst = np.nan_to_num(sst)
        ssha = np.nan_to_num(ssha)
        wind_v = np.stack(
            [
                ndimage.rotate(wind_v[:, :, 0], rot_angle, cval=np.nan),
                ndimage.rotate(wind_v[:, :, 1], rot_angle, cval=np.nan),
            ],
            axis=-1,
        )
        wind_v = ma.masked_invalid(wind_v)
        tsc_v = np.stack(
            [
                ndimage.rotate(tsc_v[:, :, 0], rot_angle, cval=np.nan),
                ndimage.rotate(tsc_v[:, :, 1], rot_angle, cval=np.nan),
            ],
            axis=-1,
        )
        tsc_v = ma.masked_invalid(tsc_v)
        rot_m = np.array(
            [
                [np.cos(np.radians(rot_angle)), np.sin(np.radians(rot_angle))],
                [-np.sin(np.radians(rot_angle)), np.cos(np.radians(rot_angle))],
            ]
        )
        wind_v = np.einsum("lk,ijk->ijl", rot_m, wind_v)
        tsc_v = np.einsum("lk,ijk->ijl", rot_m, tsc_v)
        sst = ndimage.rotate(sst, rot_angle, cval=np.nan)
        sst = ma.masked_invalid(sst)
        ssha = ndimage.rotate(ssha, rot_angle, cval=np.nan)
        ssha = ma.masked_invalid(ssha)
        lat = ndimage.rotate(lat, rot_angle, mode="nearest")
        lon = ndimage.rotate(lon, rot_angle, mode="nearest")
    dic_out = {
        "tsc": tsc_v,
        "wnd": wind_v,
        "sst": sst,
        "ssha": ssha,
        "lon": lon,
        "lat": lat,
        "grid_spacing": smp_out,
    }
    return dic_out, smp_out


def dummy_wind_adjustment(u_in, v_in):
    return 0.95 * u_in, 0.95 * v_in


def read_scenario_DALES_KNMI(
    ncfile,
    smp_out=500,
    wind_adjustment_func=dummy_wind_adjustment,
    SST0=292,
    rot_angle: Optional[float] = 0,
    add_margin=22e3,
):
    swind = xr.open_dataset(ncfile)
    dx = 1e3 * (swind.cross_track.values[1] - swind.cross_track.values[0])
    u = np.flip(np.transpose(swind.U10.values), axis=1)
    v = np.flip(np.transpose(swind.V10.values), axis=1)
    z = np.flip(np.transpose(swind.Wind_height.values), axis=1)
    u, v = wind_adjustment_func(u, v)
    w = np.flip(np.transpose(swind.w10.values), axis=1)
    lat = np.flip(np.transpose(swind.latitude.values), axis=1)
    lon = np.flip(np.transpose(swind.longitude.values), axis=1)
    if int(np.floor(smp_out / dx)) > 1:
        dec = int(np.floor(smp_out / dx))
        smp_out = dec * dx
        smp0 = int(dec / 2)
        u = drtls.smooth(u, dec)
        v = drtls.smooth(v, dec)
        w = drtls.smooth(w, dec)
        u = u[smp0:-1:dec, smp0:-1:dec]
        v = v[smp0:-1:dec, smp0:-1:dec]
        w = w[smp0:-1:dec, smp0:-1:dec]
        lat = lat[smp0:-1:dec, smp0:-1:dec]
        lon = lon[smp0:-1:dec, smp0:-1:dec]

    if int(add_margin / smp_out) > 0:
        shp = u.shape
        asmpl = int(add_margin / smp_out)
        shp_out = (shp[0] + 2 * asmpl, shp[1] + 2 * asmpl)
        u_ = np.zeros(shp_out) + np.mean(u)
        u_[asmpl : asmpl + shp[0], asmpl : asmpl + shp[1]] = u
        u = u_
        v_ = np.zeros(shp_out) + np.mean(v)
        v_[asmpl : asmpl + shp[0], asmpl : asmpl + shp[1]] = v
        v = v_

        lat_ = np.arange(shp_out[0]) * (lat[1, 0] - lat[0, 0])
        lat = lat_.reshape((shp_out[0], 1)) + np.zeros_like(u) - lat_[asmpl] + lat[0, 0]
        lon_ = np.arange(shp_out[1]) * (lon[0, 1] - lon[0, 0])
        lon = lon_.reshape((1, shp_out[1])) + np.zeros_like(u) - lon_[asmpl] + lon[0, 0]

    wind_v = np.stack([u, v], axis=-1)
    tsc_v = np.zeros_like(wind_v)
    sst = np.zeros_like(u) + SST0

    if rot_angle != 0:
        wind_v[np.isnan(wind_v)] = 0
        tsc_v[np.isnan(tsc_v)] = 0
        sst[np.isnan(sst)] = 25
        wind_v = np.stack(
            [
                ndimage.rotate(wind_v[:, :, 0], rot_angle),
                ndimage.rotate(wind_v[:, :, 1], rot_angle),
            ],
            axis=-1,
        )
        tsc_v = np.stack(
            [
                ndimage.rotate(tsc_v[:, :, 0], rot_angle),
                ndimage.rotate(tsc_v[:, :, 1], rot_angle),
            ],
            axis=-1,
        )
        sst = ndimage.rotate(sst, rot_angle)
        lat = ndimage.rotate(lat, rot_angle)
        lon = ndimage.rotate(lon, rot_angle)
        rot_m = np.array(
            [
                [np.cos(np.radians(rot_angle)), np.sin(np.radians(rot_angle))],
                [-np.sin(np.radians(rot_angle)), np.cos(np.radians(rot_angle))],
            ]
        )
        wind_v = np.einsum("lk,ijk->ijl", rot_m, wind_v)
        tsc_v = np.einsum("lk,ijk->ijl", rot_m, tsc_v)

    dic_out = {
        "tsc": tsc_v,
        "wnd": wind_v,
        "sst": sst,
        "lon": lon,
        "lat": lat,
        "grid_spacing": smp_out,
    }
    return dic_out, smp_out


def read_tsc_wind_from_mat(matfile, smp_out=None):
    """
    Read tsc and wind from mat file (in Claudia Pasquero's format)
    :param matfile:
    :return:
    """
    scn = spio.loadmat(matfile)
    tsc_v = np.zeros(scn["usfc"].shape + (2,))
    wind_v = np.zeros_like(tsc_v)
    tsc_v[:, :, 0] = scn["usfc"]
    tsc_v[:, :, 1] = scn["vsfc"]
    wind_v[:, :, 0] = scn["uwind"]
    wind_v[:, :, 1] = scn["vwind"]
    lat = scn["lat"]
    lon = scn["lon"]
    dx = np.radians(lon[0, 1] - lon[0, 0]) * cnst.r_earth
    dy = np.radians(lat[1, 0] - lat[0, 0]) * cnst.r_earth
    if smp_out is None:
        smp_out = dx
    else:
        # Resample
        xo, yo = calculate_resampled_locations(tsc_v.shape, dx, dy, smp_out)
        wind_v = _resample_model_data(wind_v, xo, yo)
        tsc_v = _resample_model_data(tsc_v, xo, yo)

    return tsc_v, wind_v, smp_out


# %%

if __name__ == "__main__":

    surfwinds = "/Users/plopezdekker/Documents/WORK/STEREOID/DATA/TIR/DALES/DALES_HR_model/Dales_36_hrs_12_01_00_surface_winds.nc"
    surfwinds_130 = "/Users/plopezdekker/Documents/WORK/STEREOID/DATA/TIR/DALES/DALES_HR_model/Dales_36_hrs_12_03_10_surface_winds.nc"
    swind = xr.open_dataset(surfwinds)
    swind_130 = xr.open_dataset(surfwinds_130)
    dls, dx = read_scenario_DALES_KNMI(surfwinds, smp_out=300, rot_angle=11)
    dls
    5 / 7500
    plt.figure()
    plt.imshow(np.linalg.norm(dls["wnd"], axis=-1), origin="lower", cmap="gray")
    plt.figure()
    plt.imshow(dls["lon"], origin="lower", cmap="gray")

    # np.sin(np.radians(11))*100e3
    # %%
    main_dir = "/Users/plopezdekker/Documents/WORK/STEREOID"
    pardir = os.path.join(main_dir, "PAR")
    datadir = "/Users/plopezdekker/Documents/WORK/STEREOID/DATA/Ocean/Scenarios"
    # scn_file = 'sample_sfc_velocity_wind.mat
    scn_file = "sample_indian"
    tsc, wind, dx = read_tsc_wind_from_mat(os.path.join(datadir, scn_file), smp_out=1e3)
    # scn = spio.loadmat(os.path.join(datadir, scn_file))
    mtsc = np.linalg.norm(tsc, axis=-1)
    # mtsc = np.sqrt(scn['usfc']**2 + scn['vsfc']**2)
    mwind = np.linalg.norm(wind, axis=-1)
    # mwind = np.sqrt(scn['uwind'] ** 2 + scn['vwind'] ** 2)
    # vorticity
    # rough
    dy = dx
    xs = dx * np.arange(tsc.shape[1])
    ys = dy * np.arange(tsc.shape[0])
    dvtsc_dy, dvtsc_dx = np.gradient(tsc[:, :, 1], dy, dx)
    dutsc_dy, dutsc_dx = np.gradient(tsc[:, :, 0], dy, dx)
    vort_tsc = dvtsc_dx - dutsc_dy
    div_tsc = dutsc_dx + dvtsc_dy

    plt.figure()
    strm_tsc = plt.streamplot(
        xs / 1e3, ys / 1e3, tsc[:, :, 0], tsc[:, :, 1], color=mtsc, cmap="viridis_r"
    )
    plt.colorbar(strm_tsc.lines)
    plt.figure()

    strm_wind = plt.streamplot(
        xs / 1e3, ys / 1e3, wind[:, :, 0], wind[:, :, 1], color=mwind, cmap="viridis_r"
    )
    plt.colorbar(strm_wind.lines)

    plt.figure()
    plt.imshow(
        vort_tsc,
        origin="lower",
        extent=[xs[0] / 1e3, xs[-1] / 1e3, ys[0] / 1e3, ys[-1] / 1e3],
        vmin=-np.max(np.abs(vort_tsc)),
        vmax=np.max(np.abs(vort_tsc)),
        cmap="bwr",
    )
    plt.title("TSC vorticity")
    plt.colorbar()

    plt.figure()
    plt.imshow(
        div_tsc,
        origin="lower",
        extent=[xs[0] / 1e3, xs[-1] / 1e3, ys[0] / 1e3, ys[-1] / 1e3],
        vmin=-np.max(np.abs(div_tsc)),
        vmax=np.max(np.abs(div_tsc)),
        cmap="bwr",
    )
    plt.title("TSC divergence")
    plt.colorbar()
