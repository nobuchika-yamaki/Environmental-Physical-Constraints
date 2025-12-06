# Environmental-Physical-Constraints
V1.0
# Adaptive Dynamics Simulation
This repository contains code for simulating life-like adaptive dynamics under varying environmental physical constraints.  
The model implements a recurrent neural system with anatomical scaling, metabolic limits, temporal grain (dt), and temporal asymmetry (alpha).  
These simulations are used to evaluate how gravity, temporal resolution, and directional updating shape the viability of complex adaptive dynamics.

---

## 📦 Repository Structure

adaptive-dynamics-simulation/
│
├── model.py # Core recurrent dynamics model
├── metrics.py # Temporal integration, dimensionality, metabolic cost
├── config.py # Anatomical + metabolic scaling rules
├── run_single.py # Run one simulation with chosen parameters
├── sweep.py # Parameter sweep for gravity, dt, alpha
└── README.md

---

## 🔧 Requirements

The code requires only NumPy:

pip install numpy

Tested with **Python 3.10+**.

---

## 🚀 Running a Single Simulation

python run_single.py

This outputs a dictionary with:

- `stable`: whether metabolic constraints were satisfied  
- `integration`: temporal integration metric  
- `dimensionality`: effective dimensionality  
- `metabolic_cost`: mean absolute activity  

Example output:

```python
{
  'stable': True,
  'integration': 0.032,
  'dimensionality': 4.82,
  'metabolic_cost': 0.091
}
Parameter Sweep
To run multiple simulations across physical parameter ranges:
python sweep.py
Modify the following inside sweep.py:
gvals = np.linspace(0.2, 3.0, 5)
dtvals = [0.005, 0.01, 0.02]
avals = [0.0, 0.1, 0.2]
The sweep returns a list of dictionaries, one per simulation condition.
Model Summary
The model combines:
Anatomical scaling: size ∝ g^(-1/3)
Metabolic capacity: max power ∝ g^(1/2)
Recurrent dynamics with nonlinear activation
Temporal grain (dt) controlling discretization
Temporal asymmetry (alpha) blending symmetric and drift components
Metrics computed include:
Temporal integration
Effective dimensionality
Mean metabolic expenditure
These are used to evaluate the viability of adaptive dynamical regimes.
