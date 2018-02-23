#!/usr/bin/env python
"""
make-supercell - A quick helper script to make supercells of structure files
with ASE
"""

# Python 2-to-3 compatibility code
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os, sys
import numpy as np
import argparse as ap

from ase import io
from ase.build.supercells import make_supercell

parser = ap.ArgumentParser()
# Main argument
parser.add_argument('input_file', type=str, default=None,
                    help="File to create a supercell of")
# Optional arguments
# Boolean args
parser.add_argument('--supercell', '-sc', type=int, default=[2], nargs='+',
                    help="Supercell shape. Can be 1, 3 or 9 integers,"
                    " producing the following results: "
                    " A = make a cubic supercell with side a; "
                    " A B C = make an orthorombic supercell with sides A, B"
                    " and C; "
                    " AA AB AC BA BB BC CA CB CC = make a generic supercell"
                    " using a matrix defined by the given components")
parser.add_argument('--output', '-o', type=str, default=None,
                    help="Output file name (including extension - "
                    "if not given a default name will be created from the "
                    "input one)")

args = parser.parse_args()

# Input structure
struct = io.read(args.input_file)

# Build the supercell matrix
scell_arg = np.array(args.supercell)
if scell_arg.shape not in ((1,), (3,), (9,)):
    sys.exit('Invalid supercell argument shape '
             '(use either 1, 3 or 9 numbers)')

if scell_arg.shape == (1,):
    scell_mat = np.eye(3)*scell_arg[0]
elif scell_arg.shape == (3,):
    scell_mat = np.diag(scell_arg)
else:
    scell_mat = scell_arg.reshape((3,3))

struct_scell = make_supercell(struct, scell_mat)

# Create output file name if needed
if args.output == None:
    ofile = '-scell'.join(os.path.splitext(args.input_file))
else:
    ofile = args.output

io.write(ofile, struct_scell)