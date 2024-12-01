import numpy as np
import matplotlib.pyplot as plt

import markov_chain

if __name__ == '__main__':

    # A) Transition matrix
    transition_matrix = np.array([
        [0.64, 0.32, 0.04],
        [0.4, 0.5, 0.1],
        [0.25, 0.5, 0.25]
    ])
    print("A: ", transition_matrix)

    # B) Calculate the border state
    border_state = markov_chain.get_border_state(transition_matrix)
    print("B: ", border_state)

    # C) Check convergence criteria
    e = 0.0000000000000000000001

    iterations = markov_chain.conv_check(transition_matrix, e)
    print("C: The matrix converges after ", iterations, " iterations.")

    # D) Transition probability
    probability_results = []
    max_iterations = 30

    transition_pair = (0, 1)

    for i in range(max_iterations):
        probability = markov_chain.transition_probability(transition_pair, i,
                                                          transition_matrix)
        probability_results.append(probability)

    markov_chain.print_plot(probability_results, border_state[transition_pair[1]],
                            f"Transition probability from state {transition_pair[0]}"
                            f" to state {transition_pair[1]} over time")
