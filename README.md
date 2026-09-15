# Agent Based Model 1

Agent based model simulating the emergence of drug resistance through horizontal gene transfer during milk aggregation, transport and storage.

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

## Model workflow

Farm → Transport → Storage → Raw milk supply or Processing entry

## Main experiment

The HGT probability was evaluated at 0, 0.05, 0.10, and 0.20, with 50 simulation runs for each probability.

The model was developed in Python using Mesa, NumPy, pandas, and Matplotlib.

## Reproducibility

The scripts and analysis code used for ABM 1 are provided in this repository to support reproducibility of the reported analysis.


