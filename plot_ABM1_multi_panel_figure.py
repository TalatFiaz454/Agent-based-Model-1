import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# LOAD DATA
# =====================================

summary_df = pd.read_csv("ABM1_HGT_Sweep_Summary.csv")
runs_df = pd.read_csv("ABM1_HGT_Sweep_AllRuns.csv")

# ===== SET THESE =====
LAB_MULTI_AMR = 0.40
FINAL_HGT = 0.10   # <-- Change after calibration decision

# =====================================
# CREATE MULTI PANEL FIGURE
# =====================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# =====================================
# PANEL A — HGT Calibration Curve
# =====================================

ax = axes[0]

ax.errorbar(
    summary_df["HGT"],
    summary_df["Mean_Combined"],
    yerr=summary_df["Std_Combined"],
    marker="o",
    capsize=5
)

ax.axhline(LAB_MULTI_AMR, linestyle="--")

ax.set_xlabel("HGT Probability")
ax.set_ylabel("Multi-AMR Fraction")
ax.set_title("A. HGT Calibration Curve")
ax.grid(True)

# =====================================
# PANEL B — Distribution Shift
# =====================================

ax = axes[1]

subset = runs_df[runs_df["HGT"].isin([0.0, FINAL_HGT])]

vals_off = subset[subset["HGT"] == 0.0]["Combined_Multi_AMR"]
vals_on = subset[subset["HGT"] == FINAL_HGT]["Combined_Multi_AMR"]

ax.hist(vals_off, bins=15, alpha=0.6, label="HGT OFF")
ax.hist(vals_on, bins=15, alpha=0.6, label=f"HGT {FINAL_HGT}")

ax.set_xlabel("Multi-AMR Fraction")
ax.set_ylabel("Frequency")
ax.set_title("B. Emergence With HGT Activation")
ax.legend()

# =====================================
# PANEL C — Raw vs Processing Neutrality
# =====================================

ax = axes[2]

subset = runs_df[runs_df["HGT"] == FINAL_HGT]
diff = subset["Raw_Multi_AMR"] - subset["Proc_Multi_AMR"]

ax.hist(diff, bins=15)
ax.axvline(0, linestyle="--")

ax.set_xlabel("Raw − Processing Multi-AMR")
ax.set_ylabel("Frequency")
ax.set_title("C. Pathway Neutrality Check")

# =====================================
# FINALIZE
# =====================================

plt.tight_layout()

plt.savefig(
    "FIG_ABM1_MultiPanel_Validation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Saved: FIG_ABM1_MultiPanel_Validation.png")
plt.savefig("ABM1_Figure.png", dpi=300, bbox_inches='tight')