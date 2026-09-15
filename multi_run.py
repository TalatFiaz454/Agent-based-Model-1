
print("Script started")
# import numpy as np
# from model import MilkAMR_ABM1
#
# N_RUNS = 50
#
# raw_vals = []
# proc_vals = []
#
# for seed in range(N_RUNS):
#     model = MilkAMR_ABM1(
#         n_farms=30,
#         batches_per_farm=6,
#         raw_milk_fraction=0.5,
#         growth_rate=0.4,
#         hgt_probability=0.1,
#         seed=seed
#     )
#
#     for _ in range(3):
#         model.step()
#
#     results = model.get_outputs()
#
#     raw_vals.append(results["raw_milk_supply"]["fraction_multi_amr"])
#     proc_vals.append(results["processing_entry"]["fraction_multi_amr"])
#
# raw_vals = np.array(raw_vals)
# proc_vals = np.array(proc_vals)
#
# diff = raw_vals - proc_vals
#
# print("Runs where raw > processing:", np.sum(diff > 0), "/", N_RUNS)
# print("Mean difference (raw − processing):", np.mean(diff))
# print("Std of difference:", np.std(diff))

import numpy as np
import pandas as pd
from model import MilkAMR_ABM1

# =====================================
# EXPERIMENT SETTINGS
# =====================================

HGT_VALUES = [0.0, 0.05, 0.1, 0.2]
N_RUNS = 50
N_STEPS = 3

# Storage containers
summary_rows = []
all_run_rows = []

# =====================================
# HGT SWEEP LOOP
# =====================================

for hgt in HGT_VALUES:

    raw_vals = []
    proc_vals = []

    print("\n====================================")
    print(f"Running HGT Probability = {hgt}")
    print("====================================")

    for seed in range(N_RUNS):

        model = MilkAMR_ABM1(
            n_farms=30,
            batches_per_farm=6,
            raw_milk_fraction=0.5,
            growth_rate=0.4,
            hgt_probability=hgt,
            seed=seed
        )

        for _ in range(N_STEPS):
            model.step()

        outputs = model.get_outputs()

        raw_frac = outputs["raw_milk_supply"]["fraction_multi_amr"]
        proc_frac = outputs["processing_entry"]["fraction_multi_amr"]

        raw_vals.append(raw_frac)
        proc_vals.append(proc_frac)

        all_run_rows.append({
            "HGT": hgt,
            "Seed": seed,
            "Raw_Multi_AMR": raw_frac,
            "Proc_Multi_AMR": proc_frac,
            "Combined_Multi_AMR": np.mean([raw_frac, proc_frac])
        })

    # Convert arrays
    raw_vals = np.array(raw_vals)
    proc_vals = np.array(proc_vals)

    combined_vals = np.mean([raw_vals, proc_vals], axis=0)
    diff = raw_vals - proc_vals

    # Summary stats
    summary_rows.append({
        "HGT": hgt,
        "Mean_Raw": np.mean(raw_vals),
        "Mean_Proc": np.mean(proc_vals),
        "Mean_Combined": np.mean(combined_vals),
        "Std_Combined": np.std(combined_vals),
        "Raw_GT_Proc_Count": int(np.sum(diff > 0))
    })

    # Console output (like your original script)
    print("Runs where raw > processing:", np.sum(diff > 0), "/", N_RUNS)
    print("Mean Raw Multi-AMR:", np.mean(raw_vals))
    print("Mean Proc Multi-AMR:", np.mean(proc_vals))
    print("Mean Combined Multi-AMR:", np.mean(combined_vals))
    print("Std Combined Multi-AMR:", np.std(combined_vals))

# =====================================
# SAVE RESULTS
# =====================================

df_summary = pd.DataFrame(summary_rows)
df_all_runs = pd.DataFrame(all_run_rows)

df_summary.to_csv("ABM1_HGT_Sweep_Summary.csv", index=False)
df_all_runs.to_csv("ABM1_HGT_Sweep_AllRuns.csv", index=False)

print("\n====================================")
print("HGT Sweep Completed")
print("Saved:")
print("  ABM1_HGT_Sweep_Summary.csv")
print("  ABM1_HGT_Sweep_AllRuns.csv")
print("====================================")
