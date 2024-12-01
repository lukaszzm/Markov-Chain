import numpy as np

import markov_chain
import transitions

def solve(transition_matrix: [[float]], start: int, end: int):
    simulation_arr = markov_chain.simulate(start, transition_matrix)
    exp_border_state = simulation_arr[-1]

    markov_chain.print_plot(simulation_arr, exp_border_state,
                            f"Starting from state {start}")

    fixed_exp_border_state = exp_border_state[end]
    fixed_simulation_arr = []

    for i in range(len(simulation_arr)):
        fixed_simulation_arr.append(simulation_arr[i][end])

    print(f"Starting from state {start}, the expected border state is "
          f"{fixed_exp_border_state}")

    markov_chain.print_plot(fixed_simulation_arr, fixed_exp_border_state,
                            f"Starting from state {start}, "
                            f"probability for {end} connected ")


if __name__ == '__main__':
    users = 100
    transition_matrix = transitions.construct(users)

    solve(transition_matrix, 0, 20)




