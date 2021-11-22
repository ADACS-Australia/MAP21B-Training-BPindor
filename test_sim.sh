#! /usr/bin/env bash

echo "Testing sim.py"
python sim.py || { echo "FAILED to run with default parameters"; exit 1 ;}
python sim.py --help || { echo "FAILED to print help"; exit 1 ;}

python sim.py --out test.csv
if [ ! -f "test.csv" ]; then
    echo "FAILED to generate ouput test.csv"
    exit 1
fi

echo "all tests PASSED"
exit 0