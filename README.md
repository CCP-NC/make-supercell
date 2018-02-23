# make-supercell
A quick helper script to make supercells of structure files with ASE

### Installation

Download or clone the folder, then from the parent path install with:

    pip install --user make-supercell/

This should automatically install also all necessary dependencies. The script can now be used in the command line from anywhere in the system.

### Usage

The default usage with a single input file, like for example:

    make-supercell.py test.cif

will produce by default a `test-scell.cif` output file with a 2x2x2 supercell. To control the size of the supercell one can use the `--supercell` (or `-sc`) argument:

* `-sc A` will produce a cubic supercell of side A;
* `-sc A B C` will produce an orthorombic supercell repeated A, B, C times along each respective axis;
* `-sc AA AB AC BA BB BC CA CB CC` will produce a generic supercell defined by a matrix.

In the latter case, the matrix will be arranged as:

    ----------------
    | AA | AB | AC |
    ----------------
    | BA | BB | BC |
    ----------------
    | CA | CB | CC |
    ----------------

It is also possible to control the name of the output file with the `--output` (or `-o`) option. The file name must be complete with extension. If the format is supported by ASE, this allows to write output files in a different format from the input.
