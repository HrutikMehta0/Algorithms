# Doomsday Fuel
# =============

# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as
# raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form.
# There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state
# of a given ore sample. You have carefully studied the different structures that the ore can take and which
# transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed.
# That is, each time the ore is in 1 state, it has the same probabilities of entering the next state
# (which might be the same state).  You have recorded the observed transitions in a matrix.
# The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state
# has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each
# terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in
# simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a
# path from that state to a terminal state. That is, the processing will always eventually end in a stfable state.
# The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation,
# as long as the fraction is simplified regularly.

# For example, consider the matrix m:
# [
#  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#  [0,0,0,0,0,0],  # s3 is terminal
#  [0,0,0,0,0,0],  # s4 is terminal
#  [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is [0, 3, 2, 9, 14].
from fractions import Fraction


def solution(m):
    # Your code here
    # Find the terminal states
    terminal_states = []
    transition_states = []
    for i in range(len(m)):
        if sum(m[i]) == 0:
            terminal_states.append(i)
        else:
            transition_states.append(i)

    # Create the transition matrix
    transition_matrix = m
    l = len(m)
    for i in range(l):
        row_sum = sum(m[i])
        if row_sum == 0:
            transition_matrix[i][i] = 1
        else:
            for j in range(l):
                transition_matrix[i][j] = Fraction(m[i][j], row_sum)

    # Standardize the transition matrix
    q = []
    for row in transition_states:
        current_row = []
        for col in transition_states:
            current_row.append(m[row][col])
        q.append(current_row)
    r = []
    for row in transition_states:
        current_row = []
        for col in terminal_states:
            current_row.append(m[row][col])
        r.append(current_row)
    im = make_identity(len(q))
    # Subtract the identity matrix from q
    for i in range(len(q)):
        for j in range(len(q)):
            q[i][j] -= im[i][j]

    # Invert q
    q_inverse = invert_matrix(q)

    # Multiply q_inverse by r
    fr = matrix_multiply(q_inverse, r)

    # Convert to fractions
    for i in range(len(fr)):
        for j in range(len(fr)):
            fr[i][j] = Fraction(fr[i][j]).limit_denominator()

    # Find the lcm of the denominators
    denominator = lcm_for_arrays([item.denominator for item in fr[0]])
    result = [-1*item.numerator * denominator // item.denominator for item in fr[0]]
    result.append(denominator)
    return result


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def make_2d_list(n, m):
    a = []
    for row in range(n):
        a += [[0] * m]
    return a


def make_identity(n):
    matrix = make_2d_list(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def lcm(a, b):
    result = a * b // gcd(a, b)
    return result


def lcm_for_arrays(args):
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)

    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial


def multiply_row_of_square_matrix(matrix, row, k):
    n = len(matrix)
    identity = make_identity(n)
    identity[row][row] = k
    return matrix_multiply(identity, matrix)


def add_multiple_of_row_of_square_matrix(matrix, source_row, k, target_row):
    n = len(matrix)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return matrix_multiply(row_operator, matrix)


def invert_matrix(matrix):
    n = len(matrix)
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        k = Fraction(1, matrix[diagonal_row][col])
        matrix = multiply_row_of_square_matrix(matrix, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -matrix[target_row][col]
                matrix = add_multiple_of_row_of_square_matrix(matrix, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse


def matrix_multiply(a, b):
    # Matrix multiplication
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


# Test cases
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == [7, 6, 8, 21])
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14])
