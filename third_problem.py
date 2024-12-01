import numpy as np

import markov_chain
import transitions

if __name__ == '__main__':
    users = 100
    transition_matrix = transitions.construct(users)

    starting_point = 0

    simulation_arr = markov_chain.simulate(starting_point, transition_matrix)
    exp_border_state = simulation_arr[-1]

    state_index = np.argmax(exp_border_state)

    fixed_exp_border_state = exp_border_state[state_index]
    fixed_simulation_arr = []

    for i in range(len(simulation_arr)):
        fixed_simulation_arr.append(simulation_arr[i][state_index])

    print(f"Starting from state {starting_point}, the expected border state is "
          f"{fixed_exp_border_state}")

    markov_chain.print_plot(fixed_simulation_arr, fixed_exp_border_state,
                            f"Starting from state {starting_point}, "
                            f"probability for {state_index} connected ")


