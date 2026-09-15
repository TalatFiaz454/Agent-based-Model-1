from mesa import Model
from mesa.time import RandomActivation
from agents import MilkBatchAgent
import random
import numpy as np


class MilkAMR_ABM1(Model):
    """
    ABM-1: AMR emergence before processing with raw vs processed branching
    """

    def __init__(
        self,
        n_farms=20,
        batches_per_farm=5,
        rare_high_amr_farms=0.1,
        raw_milk_fraction=0.4,     # NEW
        growth_rate=0.35,
        hgt_probability=0.15,
        hgt_density_threshold=5e5,
        seed=None
    ):
        super().__init__(seed=seed)

        self.schedule = RandomActivation(self)

        self.growth_rate = growth_rate
        self.hgt_probability = hgt_probability
        self.hgt_density_threshold = hgt_density_threshold
        self.raw_milk_fraction = raw_milk_fraction

        self.mixing_pool = []

        farm_ids = list(range(n_farms))
        high_amr_farms = random.sample(
            farm_ids,
            int(n_farms * rare_high_amr_farms)
        )

        for farm in farm_ids:
            for _ in range(batches_per_farm):
                amr_genes = random.choice([0, 1, 2])
                if farm in high_amr_farms:
                    amr_genes = random.choice([2, 3])

                bacterial_load = random.uniform(1e3, 1e4)

                agent = MilkBatchAgent(
                    self,
                    farm_id=farm,
                    amr_genes=amr_genes,
                    bacterial_load=bacterial_load
                )

                self.schedule.add(agent)

    def step(self):
        self.mixing_pool = [
            a for a in self.schedule.agents
            if a.stage == "transport"
        ]
        self.schedule.step()

    def get_outputs(self):
        processing = []
        raw = []

        for a in self.schedule.agents:
            if a.final_pathway == "processing_entry":
                processing.append(a.amr_genes)
            elif a.final_pathway == "raw_milk_supply":
                raw.append(a.amr_genes)

        return {
            "processing_entry": {
                "fraction_multi_amr": np.mean([g > 2 for g in processing]) if processing else 0,
                "mean_amr": np.mean(processing) if processing else 0,
                "count": len(processing)
            },
            "raw_milk_supply": {
                "fraction_multi_amr": np.mean([g > 2 for g in raw]) if raw else 0,
                "mean_amr": np.mean(raw) if raw else 0,
                "count": len(raw)
            }
        }
