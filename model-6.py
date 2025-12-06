import numpy as np

class AdaptiveDynamicsModel:
    """
    Recurrent network with:
      - metabolic cost constraint
      - anatomical scaling (radius)
      - temporal grain (dt)
      - temporal asymmetry (alpha)
    """

    def __init__(self, N, R, dt, alpha, metabolic_max):
        self.N = N
        self.R = R
        self.dt = dt
        self.alpha = alpha
        self.metabolic_max = metabolic_max

        rng = np.random.default_rng(0)
        W0 = rng.normal(0, 1/np.sqrt(N), size=(N, N))
        self.W = (1 - alpha) * 0.5 * (W0 + W0.T) + alpha * W0

    def step(self, x):
        return x + self.dt * np.tanh(self.W @ x)

    def run(self, steps, x0=None):
        if x0 is None:
            x = np.random.normal(0, 0.1, self.N)
        else:
            x = x0.copy()

        xs = np.zeros((steps, self.N))

        for t in range(steps):
            x = self.step(x)
            xs[t] = x

            cost = np.mean(np.abs(x))
            if cost > self.metabolic_max:
                return xs[:t], False

        return xs, True
