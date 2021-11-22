#! /usr/bin/env python
# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import numpy as np
import math
import argparse


def generate_positions(ref_ra='00:42:44.3',
                       ref_dec='41:16:09',
                       radius=1.,
                       nsources=1000):
    """
    Create nsources random locations within radius of the reference position.

    Parameters
    ----------
    ref_ra, ref_dec : str
        Reference position in "HH:MM:SS.S"/"DD:MM:SS.S" format.
        Default position is Andromeda galaxy.

    radius : float
        The radius within which to generate positions. Default = 1.

    nsources : int
        The number of positions to generate

    Returns
    -------
    ra, dec : numpy.array
        Arrays of ra and dec coordinates in degrees.
    """

    # convert DMS -> degrees
    d, m, s = ref_dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    # convert HMS -> degrees
    h, m, s = ref_ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)  # don't forget projection effects

    ra_offsets = np.random.uniform(-1*radius, radius, size=nsources)
    dec_offsets = np.random.uniform(-1*radius, radius, size=nsources)

    ras = ra + ra_offsets
    decs = dec + dec_offsets
    return ras, decs


def write_file(ras, decs,
               outfile='catalog.csv'):
    """
    Write the ra/dec catalog to a file, and include a header and IDs.

    Parameters
    ----------
    ras, decs : list, numpy.array, or any iterable
        Iterable of ra and dec coordinates. The length of these need to match.

    outfile : str
        Path/filename for the output file. (Overwite=True)
    """
    with open(outfile, 'w') as f:
        # creat a header row
        print("id,ra,dec", file=f)
        for i in range(len(ras)):
            # use a csv format
            print("{0}, {1:7.4f}, {2:7.4f}".format(i, ras[i], decs[i]), file=f)
    return


if __name__ == '__main__':
    # Set up the parser with all the options that you want
    parser = argparse.ArgumentParser(prog='sim')
    group1 = parser.add_argument_group()
    group1.add_argument('--ref_ra', dest='ref_ra', type=str, default='00:42:44.3',
                        help='Central/reference RA position HH:MM:SS.S format')
    group1.add_argument('--ref_dec', dest='ref_dec', type=str, default='41:16:09',
                        help='Central/reference Dec position DD:MM:SS.S format')
    group1.add_argument('--radius', dest='radius', type=float, default=1.,
                        help='radius within which the new positions are generated (deg)')
    group1.add_argument('--n', dest='nsources', type=int, default=1_000,
                        help='Number of positions to generate')
    group1.add_argument('--out', dest='outfile', type=str, default='catalog.csv',
                        help='Filename for saving output (csv format)')

    # parse the command line input
    options = parser.parse_args()

    ras, decs = generate_positions(ref_ra=options.ref_ra,
                                   ref_dec=options.ref_dec,
                                   radius=options.radius,
                                   nsources=options.nsources)
    write_file(ras, decs, outfile=options.outfile)
