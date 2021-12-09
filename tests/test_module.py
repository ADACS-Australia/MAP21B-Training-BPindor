#! /usr/bin/env python3
"""
Tests for the skysim module
"""


def test_module_import():
    try:
        import skysim
    except Exception as e:
        raise AssertionError("Failed to import skysim")
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
