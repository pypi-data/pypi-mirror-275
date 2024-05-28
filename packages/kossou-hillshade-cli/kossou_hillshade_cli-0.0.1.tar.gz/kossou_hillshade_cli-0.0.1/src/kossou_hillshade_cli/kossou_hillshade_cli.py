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

from kossou_hillshade_base import (AZIMUTH, ALTITUDE, WIDTH, HEIGHT,
                                   DEFAULT_ELEVATION_TIFF, REPORT,
                                   plot_hillshade, generate_report)


# Functions ====================================================================

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
            DEFAULT_ELEVATION_TIFF,
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
