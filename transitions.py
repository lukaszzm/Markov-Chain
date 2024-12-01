import numpy as np
from scipy.special import comb


def t_probability(n: int, x: int, y: int,
                  p_log: float = 0.2,
                  p_stay_not_logged: float = 0.8,
                  p_logout: float = 0.5,
                  p_stay_logged: float = 0.5):
    prob = 0

    for k in range(n - x + 1):
        for m in range(x + 1):
            if x + k - m == y:
                prob_k = comb(n - x, k) * (p_log ** k) * (
                            p_stay_not_logged ** (n - x - k))
                prob_m = comb(x, m) * (p_logout ** m) * (p_stay_logged ** (x - m))
                prob += prob_k * prob_m

    return prob


def construct(users: int):
    transition_matrix = np.zeros((users + 1, users + 1))

    for x in range(users + 1):
        row_sum = 0
        for y in range(users + 1):
            transition_matrix[x, y] = t_probability(users, x, y)
            row_sum += transition_matrix[x, y]
        if not np.isclose(row_sum, 1):
            transition_matrix[x, :] /= row_sum

    return transition_matrix


def mixed_construct(users: int):
    transition_matrix = np.zeros((users + 1, users + 1))

    for x in range(users + 1):
        row_sum = 0
        for y in range(users + 1):
            transition_matrix[x, y] = t_probability(users, x, y,
                                                    p_log=0.2,
                                                    p_stay_not_logged=0.8,
                                                    p_logout=(1 - (0.008 * x + 0.1)),
                                                    p_stay_logged=(0.008 * x + 0.1))
            row_sum += transition_matrix[x, y]
        if not np.isclose(row_sum, 1):
            transition_matrix[x, :] /= row_sum

    return transition_matrix