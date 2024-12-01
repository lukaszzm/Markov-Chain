import markov_chain
import transitions

if __name__ == '__main__':
    MAX_ITERATIONS = 10_000
    starting_points = [0, 1, 2]
    transition_matrix = transitions.construct(2)

    for starting_point in starting_points:
        simulation_arr = markov_chain.simulate(starting_point, transition_matrix,
                                               MAX_ITERATIONS)
        exp_border_state = simulation_arr[-1]

        print(f"Starting from state {starting_point}, the expected border state is "
              f"{exp_border_state}")

        markov_chain.print_plot(simulation_arr, exp_border_state,
                                f"Starting from state {starting_point}")
