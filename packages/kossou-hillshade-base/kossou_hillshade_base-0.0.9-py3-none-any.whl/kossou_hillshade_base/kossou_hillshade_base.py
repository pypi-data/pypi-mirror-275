#===============================================================================
# kossou_hillshade_base.py
#===============================================================================

# Imports ======================================================================

import earthpy.plot as ep
import earthpy.spatial as es
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import rasterio as rio


# Constants ====================================================================

AZIMUTH = 30
ALTITUDE = 30
WIDTH = 10.0
HEIGHT = 10.0
DEFAULT_ELEVATION_TIFF = os.path.join(
    os.path.dirname(__file__),
    'static',
    'n07_w006_3arc_v2.tif'
)
DEFAULT_COLORMAP_ELEVATION = 'terrain'
DEFAULT_COLORMAP_HILLSHADE = 'plasma'
REPORT = """Hillshade Plot
---------
Hillshade from DTM of Lake Kossou. Azimuth of sun is {azimuth}\N{DEGREE SIGN}, altitude is {altitude}\N{DEGREE SIGN}.

<img src="{hillshade_jpg}" width="400" />
"""

# Functions ====================================================================

def plot_elevation(
    input_dtm: str,
    output_file: str,
    width: float = WIDTH,
    height: float = HEIGHT,
    title=None,
    colormap: str = DEFAULT_COLORMAP_ELEVATION
):
    np.seterr(divide='ignore', invalid='ignore')
    with rio.open(input_dtm) as src:
        elevation = src.read(1)
    _, ax = plt.subplots(figsize=(width, height))
    ep.plot_bands(elevation, ax=ax, cbar=True, cmap=colormap, title=title)
    plt.savefig(output_file, dpi=300)


def plot_hillshade(
    input_dtm: str,
    output_file: str,
    azimuth: int = AZIMUTH,
    altitude: int = ALTITUDE,
    width: float = WIDTH,
    height: float = HEIGHT,
    title=None,
    colormap: str = DEFAULT_COLORMAP_HILLSHADE
):
    np.seterr(divide='ignore', invalid='ignore')
    with rio.open(input_dtm) as src:
        elevation = src.read(1)
    hillshade = es.hillshade(elevation, azimuth=azimuth, altitude=altitude)
    _, ax = plt.subplots(figsize=(width, height))
    ep.plot_bands(hillshade, ax=ax, cbar=True, cmap=colormap, title=title)
    plt.savefig(output_file, dpi=300)
    # fig = ax.get_figure()
    # fig.tight_layout()
    # fig.savefig(output_file, format='jpg', dpi=300)
    # fig.clf()


def generate_report(
    output_file = 'hillshade.jpg',
    azimuth: int = AZIMUTH,
    altitude: int = ALTITUDE
):
    return REPORT.format(azimuth=azimuth, altitude=altitude, hillshade_jpg=output_file)
