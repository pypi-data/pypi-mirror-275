#===============================================================================
# kossou_hillshade_base.py
#===============================================================================

# Imports ======================================================================

import earthpy.plot as ep
import earthpy.spatial as es
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
import misaka as m
import numpy as np
import os
import os.path
import rasterio as rio

from argparse import ArgumentParser


# Constants ====================================================================

AZIMUTH = 30
ALTITUDE = 30
WIDTH = 10.0
HEIGHT = 10.0

REPORT = """Hillshade Plot
---------
Hillshade from DTM of Lake Kossou. Azimuth of sun is {azimuth}\N{DEGREE SIGN}, altitude is {altitude}\N{DEGREE SIGN}.

<img src="{hillshade_jpg}" width="400" />
"""

# Functions ====================================================================

def plot_hillshade(
    input_dtm: str,
    output_file: str,
    azimuth: int = AZIMUTH,
    altitude: int = ALTITUDE,
    width: float = WIDTH,
    height: float = HEIGHT,
    title=None
):
    np.seterr(divide='ignore', invalid='ignore')
    with rio.open(input_dtm) as src:
        elevation = src.read(1)
    hillshade = es.hillshade(elevation, azimuth=azimuth, altitude=altitude)
    _, ax = plt.subplots(figsize=(width, height))
    ep.plot_bands(
        hillshade,
        ax=ax,
        cbar=True,
        cmap="plasma",
        title=title
    )
    plt.savefig(output_file, dpi=300)
    # fig = ax.get_figure()
    # fig.tight_layout()
    # fig.savefig(output_file, format='jpg', dpi=300)
    # fig.clf()

def generate_report(output_file = 'hillshade.jpg', azimuth: int = AZIMUTH, altitude: int = ALTITUDE):
    return REPORT.format(azimuth=azimuth, altitude=altitude, hillshade_jpg=output_file)

def parse_arguments():
    parser = ArgumentParser(description='Elevation data')
    parser.add_argument(
        'report_dir',
        metavar='<path/to/report/dir/>',
        nargs='?',
        help='write a HTML report'
    )
    parser.add_argument(
        '--azimuth',
        metavar='int',
        default=AZIMUTH,
        help='azimuth of sun'
    )
    parser.add_argument(
        '--altitude',
        metavar='int',
        default=ALTITUDE,
        help="angle altitude of sun"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    if not args.report_dir:
        report_text = generate_report(
            azimuth=args.azimuth,
            altitude=args.altitude
        )
        print(report_text, end='')
    else:
        report_text = generate_report(
            azimuth=args.azimuth,
            altitude=args.altitude
        )
        if not os.path.isdir(args.report_dir):
            os.mkdir(args.report_dir)
        plot_hillshade(
            os.path.join(os.path.dirname(__file__), 'static', 'n07_w006_3arc_v2.tif'),
            os.path.join(args.report_dir, 'hillshade.jpg'),
            azimuth=args.azimuth,
            altitude=args.altitude,
            title=f"Hillshade from DTM of Lake Kossou. Azimuth of sun is {args.azimuth} \N{DEGREE SIGN}, altitude is {args.altitude} \N{DEGREE SIGN}.",
        )
        with open(os.path.join(args.report_dir, 'kossou-hillshade.html'), 'w') as f:
            f.write(m.html(report_text, extensions=['tables']))


# Execute ======================================================================

if __name__ == '__main__':
    main()
