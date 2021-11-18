# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import numpy as np
import math
# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/math.cos(dec*math.pi/180)

# make 1000 stars within 1 degree of Andromeda
ra_offsets = np.random.uniform(-1, 1, size=1000)
dec_offsets = np.random.uniform(-1, 1, size=1000)

ras = ra + ra_offsets
decs = dec + dec_offsets

# now write these to a csv file for use by my other program
with open('catalog.csv', 'w') as f:
    print("id, ra, dec", file=f)
    for i in range(1000):
        print("{0}, {1:7.4f}, {2:7.4f}".format(i, ras[i], decs[i]), file=f)
