#! /usr/bin/env python

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def read_file():
    """
    """
    fname = 'catalog.csv'
    df = pd.read_csv(fname)
    return df['ra'].values, df['dec'].values


def plot(ra, dec):
    """
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.scatter(ra, dec)
    ax.set_ylabel("DEC (deg)")
    ax.set_xlabel("RA (deg")
    ax.set_title("catalog")
    plt.savefig('plot.png')


ra, dec = read_file()
plot(ra, dec)
