from model import MilkAMR_ABM1

model = MilkAMR_ABM1(
    n_farms=30,
    batches_per_farm=6,
    raw_milk_fraction=0.5,
    growth_rate=0.4,
    hgt_probability=0.2
)

for _ in range(3):
    model.step()

results = model.get_outputs()

print("\n=== ABM-1 OUTPUTS ===")

for pathway, data in results.items():
    print(f"\nPathway: {pathway}")
    print(f"  Batches: {data['count']}")
    print(f"  Mean AMR genes: {data['mean_amr']:.2f}")
    print(f"  Fraction multi-AMR (>2): {data['fraction_multi_amr']:.2f}")
