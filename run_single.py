import numpy as np
from model import AdaptiveDynamicsModel
from metrics import temporal_integration, effective_dimensionality, metabolic_cost
from config import anatomical_radius, metabolic_max_power, network_size

def run_simulation(g=1.0, dt=0.01, alpha=0.1, steps=5000):
    R = anatomical_radius(g)
    N = network_size(R)
    metabolic_max = metabolic_max_power(g)

    model = AdaptiveDynamicsModel(N=N, R=R, dt=dt, alpha=alpha, metabolic_max=metabolic_max)
    xs, stable = model.run(steps)

    if not stable:
        return {"stable": False}

    return {
        "stable": True,
        "integration": temporal_integration(xs),
        "dimensionality": effective_dimensionality(xs),
        "metabolic_cost": metabolic_cost(xs)
    }

if __name__ == "__main__":
    print(run_simulation())
