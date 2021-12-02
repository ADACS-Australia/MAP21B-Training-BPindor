# SkySim
This project was built in order to simulate source (star/galaxy/other) positions over an area of sky.

## Installing
This project relies only on python built-ins and the numpy library.
Use ```pip install -r requirements.txt``` if you don't yet meet these requirements.

## Usage
The main entry point for this project is `sim_catalog`:
```
./sim_catalog --help
usage: sim [-h] [--ref_ra REF_RA] [--ref_dec REF_DEC] [--radius RADIUS] [--n NSOURCES] [--out OUTFILE]

optional arguments:
  -h, --help         show this help message and exit

  --ref_ra REF_RA    Central/reference RA position HH:MM:SS.S format
  --ref_dec REF_DEC  Central/reference Dec position DD:MM:SS.S format
  --radius RADIUS    radius within which the new positions are generated (deg)
  --n NSOURCES       Number of positions to generate
  --out OUTFILE      Filename for saving output (csv format)
```

## Documentation
Documentation is currently just this file, and associated python docstrings.

## Author / Contribution
This project is developed by Dev One.
If you want to contribute to this project please create a fork and issue pull requests for new features or bug fixes.

## Credit
If you find this project to be useful in your academic work please cite the following paper:
[One, D. et al. Nature, 2021](https://nature.com)