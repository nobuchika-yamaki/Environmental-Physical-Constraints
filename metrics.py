import numpy as np

def temporal_integration(xs, lag=5):
    T = len(xs)
    if T <= lag:
        return 0.0
    return np.mean(np.abs(xs[lag:] - xs[:-lag]))

def effective_dimensionality(xs):
    X = xs - xs.mean(0)
    C = np.cov(X, rowvar=False)
    eigvals = np.linalg.eigvalsh(C)
    s = np.sum(eigvals)
    if s == 0:
        return 0.0
    return (s ** 2) / np.sum(eigvals ** 2)

def metabolic_cost(xs):
    return np.mean(np.abs(xs))
