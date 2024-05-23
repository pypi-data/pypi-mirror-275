# RDAnalyzer
Reactive Diffusion Analyzer (RDAnalyzer)

RDAnalyzer is a Python module for analyzing ReaxFF MD trajectory, especially the hydroxide diffusion in AEM.

Features:
- Splitting trajectory according to user's setting
- Transforming text trajectory to Atoms, Molecules, and Reactions
- Analysis based on these Atoms, Molecules, and Reactions
- Calculation of drift length of hydroxide for obtaining conductivity


## Installation
RDAnalyzer is developed on Ubuntu OS with python 3.11

RDAnalyzer needs `scipy`, `numpy`, `matplotlib`, `ase` and `networkx`,
but you always do not need install them manually when using pip to install.

**Install with pip**

```pip install -i https://test.pypi.org/simple/ RDAnalyzer-test1==0.0.1```

## Getting started
See `tests/Tutorial.ipynb` for detailed usage about RDAnalyzer 

## References
- ref