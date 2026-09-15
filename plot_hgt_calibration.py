import pandas as pd
import matplotlib.pyplot as plt

# Load summary data
df = pd.read_csv("ABM1_HGT_Sweep_Summary.csv")

# Lab anchor (EDIT THIS if needed)
LAB_MULTI_AMR = 0.40

plt.figure(figsize=(7,5))

plt.errorbar(
    df["HGT"],
    df["Mean_Combined"],
    yerr=df["Std_Combined"],
    marker="o",
    capsize=5,
    label="ABM Output"
)

plt.axhline(
    LAB_MULTI_AMR,
    linestyle="--",
    color="red",
    label="Lab Multi-AMR"
)

plt.xlabel("HGT Probability")
plt.ylabel("Multi-AMR Fraction")
plt.title("ABM-1 Calibration: HGT vs Multi-AMR")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("FIG_ABM1_HGT_Calibration.png", dpi=300)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ABM1_HGT_Sweep_AllRuns.csv")

FINAL_HGT = 0.1   # CHANGE after calibration

subset = df[df["HGT"].isin([0.0, FINAL_HGT])]

plt.figure(figsize=(7,5))

for hgt in [0.0, FINAL_HGT]:
    vals = subset[subset["HGT"] == hgt]["Combined_Multi_AMR"]
    plt.hist(vals, bins=15, alpha=0.6, label=f"HGT={hgt}")

plt.xlabel("Multi-AMR Fraction")
plt.ylabel("Frequency")
plt.title("Distribution Shift With HGT Activation")
plt.legend()

plt.tight_layout()
plt.savefig("FIG_ABM1_HGT_Distribution.png", dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ABM1_HGT_Sweep_AllRuns.csv")

FINAL_HGT = 0.1

subset = df[df["HGT"] == FINAL_HGT]

diff = subset["Raw_Multi_AMR"] - subset["Proc_Multi_AMR"]

plt.figure(figsize=(7,5))

plt.hist(diff, bins=15)
plt.axvline(0, linestyle="--", color="red")

plt.xlabel("Raw − Processing Multi-AMR")
plt.ylabel("Frequency")
plt.title("Pathway Neutrality Validation")

plt.tight_layout()
plt.savefig("FIG_ABM1_Pathway_Neutrality.png", dpi=300)
plt.show()
