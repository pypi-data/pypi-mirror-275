# BINSREG

Binscatter provides a flexible, yet parsimonious way of visualizing and summarizing large data sets and has been a popular methodology in applied microeconomics and other social sciences. The `binsreg` package provides tools for statistical analysis using the binscatter methods developed in Cattaneo, Crump, Farrell and Feng (2022). binsreg implements binscatter least squares regression with robust inference and plots, including curve estimation, pointwise confidence intervals and uniform confidence band. `binsqreg` implements binscatter quantile regression with robust inference and plots, including curve estimation, pointwise confidence intervals and uniform conf idence band. `binsglm` implements binscatter generalized linear regression with robust inference and plots, including curve estimation, pointwise confidence intervals and uniform confidence band. `binstest` implements binscatter-based hypothesis testing procedures for parametric specifications of and shape restrictions on the unknown function of interest. `binspwc` implements hypothesis testing procedures for pairwise group comparison of binscatter estimators. `binsregselect` implements data-driven number of bins selectors for binscatter implementation using either quantile-spaced or evenly-spaced binning/partitioning. All the commands allow for covariate adjustment, smoothness restrictions, and clustering, among other features.


## Authors
 
Matias D. Cattaneo (<cattaneo@princeton.edu>)

Richard K. Crump (<richard.crump@ny.frb.org>)

Max H. Farrell (<maxhfarrell@ucsb.edu>)

Yingjie Feng (<fengyingjiepku@gmail.com>)

Ricardo Masini (<rmasini@princeton.edu>)


## Website

https://nppackages.github.io/binsreg/

## Major Upgrades

This package was first released in Winter 2019, and had one major upgrade in Summer 2021.

Summer 2021 new features include: (i) generalized linear models (logit, Probit, etc.) binscatter; (ii) quantile regression binscatter; (iii) new generic specification and shape restriction hypothesis testing function (now including Lp metrics); (iv) multi-group comparison of binscatter estimators; (v) generic point evaluation of covariate-adjusted binscatter; (vi) speed improvements and optimization. A complete list of upgrades can be found [here](https://nppackages.github.io/binsreg/binsreg_upgrades.txt).


## Installation

To install/update use pip
```
pip install binsreg
```

# Usage
```
from binsreg import binsregselect, binsreg, binsqreg, binsglm, binstest, binspwc
```

- Replication: [binsreg illustration](https://github.com/nppackages/binsreg/blob/master/Python/binsreg_illustration.py), [simulated data](https://github.com/nppackages/binsreg/blob/master/Python/binsreg_sim.csv).


## Dependencies

- numpy
- pandas
- scipy
- statsmodel
- plotnine

## References

For overviews and introductions, see [NP Packages website](https://nppackages.github.io/).

### Software and Implementation

- Cattaneo, Crump, Farrell and Feng (2023c): [Binscatter Regressions](https://nppackages.github.io/references/Cattaneo-Crump-Farrell-Feng_2023_Stata.pdf).<br>
Working paper, prepared for Stata Journal.

### Technical and Methodological

- Cattaneo, Crump, Farrell and Feng (2023a): [On Binscatter](https://mdcattaneo.github.io/papers/Cattaneo-Crump-Farrell-Feng_2023_AER.pdf).<br>
Working paper.

- Cattaneo, Crump, Farrell and Feng (2023b): [Nonlinear Binscatter Methods](https://mdcattaneo.github.io/papers/Cattaneo-Crump-Farrell-Feng_2023_NonlinearBinscatter.pdf).<br>
Working paper.
