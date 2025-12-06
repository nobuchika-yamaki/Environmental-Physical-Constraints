import numpy as np
from run_single import run_simulation

def sweep(gravity_vals, dt_vals, alpha_vals):
    results = []
    for g in gravity_vals:
        for dt in dt_vals:
            for alpha in alpha_vals:
                out = run_simulation(g=g, dt=dt, alpha=alpha)
                out.update({"g": g, "dt": dt, "alpha": alpha})
                results.append(out)
    return results

if __name__ == "__main__":
    gvals = np.linspace(0.2, 3.0, 5)
    dtvals = [0.005, 0.01, 0.02]
    avals = [0.0, 0.1, 0.2]

    res = sweep(gvals, dtvals, avals)
    print(res)
