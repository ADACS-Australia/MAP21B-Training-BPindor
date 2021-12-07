#! /usr/bin/env python3
"""
Tests for the skysim.sim module
"""
import numpy as np
from skysim.sim import generate_positions


def test_negative_dec():
    """
    Test for the negative dec bug noted in issue #1
    """
    _, decs = generate_positions(ref_ra='00:00:00',
                                 ref_dec='-00:30:19',
                                 radius=0.1, nsources=10)
    if not np.all(decs < 0):
        raise AssertionError("Declinations should be <0, but are >0")
    return


if __name__ == "__main__":
    # introspect and run all the functions starting with 'test'
    for f in dir():
        if f.startswith('test'):
            try:
                globals()[f]()
            except AssertionError as e:
                print("{0} FAILED with error: {1}".format(f, e))
            else:
                print("{0} PASSED".format(f))
