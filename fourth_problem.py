import numpy as np

import markov_chain
import third_problem
import transitions

if __name__ == '__main__':
    users = 100
    transition_matrix = transitions.mixed_construct(users)

    third_problem.solve(transition_matrix, 0, 20)
