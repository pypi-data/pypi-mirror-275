# conjugate_map
Files and scripts relating to geomagnetic conjugate map. Please cite via Zenodo: [![DOI](https://zenodo.org/badge/651410906.svg)](https://zenodo.org/doi/10.5281/zenodo.10056623)

Run in Binder here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KCollins/conjugate-map/HEAD?labpath=ConjugateMap.ipynb)

There are two example notebooks available:
 - `MWE.ipynb`: Minimal working example demonstrating conjugate calculations.
 - `ConjugateMap.ipynb`: More in-depth examples using COMNAP, Madrigal and other databases to produce animated maps with plotly express.

The following functions are imported from `conjCalcFunctions.py`:
 - `findconj()` : function to compute conjugate points for a given location at a given time and date. 
 - `conjcalc()` : function to take in a dataframe and add columns for all stages of calculating conjugate points.
 - `calc_mlat_rings()` : function to calculate magnetic graticules for a given latitude and datetime.
 
 You can read the documentation for each function by running, e.g., `help(calc_mlat_rings)`.
