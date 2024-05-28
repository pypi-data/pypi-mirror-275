#===============================================================================
# kossou_hillshade_cli.py
#===============================================================================

# Imports ======================================================================

import misaka as m
import os
import os.path

from argparse import ArgumentParser

from kossou_hillshade_base import (AZIMUTH, ALTITUDE, WIDTH, HEIGHT,
                                   DEFAULT_ELEVATION_TIFF, DEFAULT_COLORMAP,
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
        '--geotiff',
        metavar='<path/to/geotiff.tif>',
        default=DEFAULT_ELEVATION_TIFF,
        help='input geotiff file'
    )
    parser.add_argument(
        '--azimuth',
        metavar='<int>',
        default=AZIMUTH,
        help='azimuth of sun'
    )
    parser.add_argument(
        '--altitude',
        metavar='<int>',
        default=ALTITUDE,
        help="angle altitude of sun"
    )
    parser.add_argument(
        '--width',
        metavar='<int>',
        default=WIDTH,
        help='width of plot in inches [10]'
    )
    parser.add_argument(
        '--height',
        metavar='<int>',
        default=HEIGHT,
        help='height of plot in inches [10]'
    )
    parser.add_argument(
        '--title',
        metavar='<"title of plot">',
        help='title of plot'
    )
    parser.add_argument(
        '--colormap',
        metavar='<"colormap">',
        default=DEFAULT_COLORMAP,
        help='colormap to use, e.g. "cividis", "plasma", or "magma" [plasma]'
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
            args.geotiff,
            os.path.join(args.report_dir, 'hillshade.jpg'),
            azimuth=args.azimuth,
            altitude=args.altitude,
            width=args.width,
            height=args.height,
            title=args.title or f"Hillshade from DTM of Lake Kossou. Azimuth of sun is {args.azimuth} \N{DEGREE SIGN}, altitude is {args.altitude} \N{DEGREE SIGN}.",
            colormap=args.colormap
        )
        with open(os.path.join(args.report_dir, 'kossou-hillshade.html'), 'w') as f:
            f.write(m.html(report_text, extensions=['tables']))


# Execute ======================================================================

if __name__ == '__main__':
    main()
