import numpy as np
from matplotlib import pyplot as plt


def simulate(startint_point: int,
             transition_matrix: [[float]],
             max_iterations: int = 10_000
             ) -> [float]:
    states_count = transition_matrix.shape[0]

    if startint_point < 0 or startint_point >= states_count:
        raise ValueError("Starting point must be a valid state")

    visits = np.zeros(states_count)
    state = startint_point
    exp_arr = []

    for step in range(1, max_iterations + 1):
        visits[state] += 1
        state = np.random.choice(states_count, p = transition_matrix[state])

        exp = visits / step
        exp_arr.append(exp)

    return exp_arr


def get_border_state(transition_matrix: [[float]]) -> [float]:
    states_length = transition_matrix.shape[0]
    left_side = transition_matrix.T - np.eye(states_length)
    left_side[-1, :] = 1
    right_side = np.zeros(states_length)
    right_side[-1] = 1
    pi = np.linalg.solve(left_side, right_side)

    return pi


def conv_check(transition_matrix: [[float]], cond: float) -> int:
    max_check = 10_000
    curr_matrix = np.linalg.matrix_power(transition_matrix, 1)

    for i in range(2, max_check):
        new_matrix = np.linalg.matrix_power(transition_matrix, i)
        diff_matrix = np.abs(new_matrix - curr_matrix)

        if np.all(diff_matrix < cond):
            return i

        curr_matrix = new_matrix

    return -1


def transition_probability(transition_to_check: (int, int), iterations: int,
                           transition_matrix: [[float]]):
    from_state = transition_to_check[0]
    to_state = transition_to_check[1]

    if iterations == 0:
        return transition_matrix[from_state][to_state]

    new_matrix = np.linalg.matrix_power(transition_matrix, iterations)
    return new_matrix[from_state][to_state]


def print_plot(results: [float], border: float, title: str):
    plt.plot(results)
    plt.plot([0, len(results)], [border, border], 'r--')
    plt.title(title)
    plt.ylabel('Probability')
    plt.xlabel('Iterations')
    plt.show()
