from mesa import Agent
import random


class MilkBatchAgent(Agent):
    """
    Milk batch carrying Pseudomonas population and AMR genes
    """

    def __init__(self, model, farm_id, amr_genes, bacterial_load):
        super().__init__(model)

        self.farm_id = farm_id
        self.amr_genes = amr_genes
        self.bacterial_load = bacterial_load

        self.stage = "farm"
        self.final_pathway = None   # raw_milk or processing

        self.amr_acquired_stage = "farm"

    def grow(self):
        self.bacterial_load *= (1 + self.model.growth_rate)

    def hgt_with(self, other):
        contact_factor = min(
            1.0,
            (self.bacterial_load + other.bacterial_load)
            / self.model.hgt_density_threshold
        )

        prob = self.model.hgt_probability * contact_factor

        if random.random() < prob:
            donor = self if self.amr_genes > other.amr_genes else other
            recipient = other if donor is self else self

            recipient.amr_genes += 1

            if recipient.amr_genes > 2 and recipient.amr_acquired_stage == "farm":
                recipient.amr_acquired_stage = recipient.stage

    def step(self):
        if self.stage == "farm":
            self.stage = "transport"

        elif self.stage == "transport":
            self.grow()

            for other in self.model.mixing_pool:
                if other is not self:
                    self.hgt_with(other)

            self.stage = "storage"

        elif self.stage == "storage":
            self.grow()

            # Branching decision
            if random.random() < self.model.raw_milk_fraction:
                self.final_pathway = "raw_milk_supply"
            else:
                self.final_pathway = "processing_entry"

            self.stage = self.final_pathway
