# Agent Based Model 1

Author: Muhammad Tulat Fiaz

Agent based model simulating the emergence of multidrug resistance through horizontal gene transfer during milk aggregation, transport and storage.

## Files

`agents.py`

Defines the milk batch agents, bacterial growth, AMR gene acquisition, and horizontal gene transfer.

`model.py`

Defines the ABM 1 milk supply chain model and its simulation parameters and outputs.

`run.py`

Runs a single demonstration simulation.

`multi_run.py`

Runs the HGT probability experiment across multiple simulations and saves the results as CSV files.

`plot_hgt_calibration.py`

Generates the HGT calibration, HGT distribution, and pathway neutrality figures.

`plot_ABM1_multi_panel_figure.py`

Generates the combined three panel validation figure.

`requirements.txt`

Lists the Python package versions required to run the model and analysis scripts.

## Model workflow

Farm → Transport → Storage → Raw milk supply or Processing entry

## Main experiment

The HGT probability was evaluated at 0, 0.05, 0.10, and 0.20, with 50 simulation runs for each probability.

The model was developed in Python using Mesa, NumPy, pandas, and Matplotlib.

## Reproducibility

The scripts and analysis code used for ABM 1 are provided in this repository to support reproducibility of the reported analysis.

## Citation

If you use this code, model, or any part of this repository in research, publications, presentations, or other academic work, please cite the associated Zenodo record and acknowledge the author.

The DOI will be added after the repository is archived by Zenodo.

Suggested citation:

Fiaz, M.T., M.H. Mushtaq, F. Awan and A. Riaz (2026). Detection of Multidrug Resistant Milk Associated Psychrotrophic Pseudomonas spp. Using Lab Based and Agent Based Modeling Approaches in Pakistan. J. Anim. Plant Sci. DOI:

## Code Use and Attribution

If you use, modify, or build upon this code, please acknowledge the original work and cite the associated DOI.

Please do not present this code, model, or substantial parts of it as your own original work.



