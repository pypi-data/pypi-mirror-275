#!/usr/bin/env python3
"""
    stldim - Get dimensions of an STL file
    Usage:
        stldim.py [options] <stlfile>

    Options:
        -h --help       Show this screen.
        --version       Show version.
        --name=<name>   Name of the object [defaults to the filename with non alpha-numeric\
characters replaced with underscores].
"""

import os
import sys

from docopt import docopt
import jinja2

from stldim import MeshWithBounds, get_varname, version

def generate_openscad_lib(stl_dimensions, varname, stlfile):
    """
    Generate an OpenSCAD library file with the dimensions of the STL file
    """
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = environment.get_template('stldim/templates/openscad_lib.jinja2')
    print(template.render(stl_dimensions=stl_dimensions, varname=varname, stlfile=stlfile))

def main():
    """
    Main function
    """
    args = docopt(__doc__, version=version.__str__)

    if not os.path.exists(args['<stlfile>']):
        sys.exit(f"ERROR: file {args['<stlfile>']} was not found!")
    varname = get_varname(args['<stlfile>'], args['--name'])

    stl_dimensions = MeshWithBounds.from_file(args['<stlfile>'])

    generate_openscad_lib(stl_dimensions, varname, args['<stlfile>'])


if __name__ == '__main__':
    main()
