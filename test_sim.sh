#! /usr/bin/env bash

echo "Testing sim.py"
./sim_catalog || { echo "FAILED to run with default parameters"; exit 1 ;}
./sim_catalog --help || { echo "FAILED to print help"; exit 1 ;}

./sim_catalog --out test.csv
if [ ! -f "test.csv" ]; then
    echo "FAILED to generate ouput test.csv"
    exit 1
fi

echo "all tests PASSED"
exit 0