def anatomical_radius(g):
    return 1.0 * g ** (-1/3)

def metabolic_max_power(g):
    return 1.0 * g ** 0.5

def network_size(R):
    return int(50 * R)
