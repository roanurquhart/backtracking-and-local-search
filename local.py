import utilityfuncs
import heapq
import random

violations_heap = []
lcl_states = {}
num_violations = 0


def local_search():
    init_lcl_states()
    rand_assign()
    init_heap()


# Randomly assigns a color value to all of the states
def rand_assign():
    for state in lcl_states.values():
        random_color = random.sample(state.colors_available, 1)
        state.set_color(random_color[0])


# Creates the heap that orders the states by amount of violations
def init_heap():
    global num_violations
    for state in lcl_states.values():
        violations = count_violations(state)
        # Negate values in order to create max heap, need to abs value values later
        heapq.heappush(violations_heap, ((-1 * violations), state.get_name()))
        num_violations += violations


# Prints the violations heap, but depopulates
def print_heap():
    index = 0
    while len(violations_heap) > 0:
        state = heapq.heappop(violations_heap)
        print(state[1] + ": " + str(state[0]))


# Counts the number of violations a state has after randomization
def count_violations(state):
    count = 0

    for ste in state.adjacentStates:
        if state.get_color() == ste.get_color():
            count += 1

    return count


# Copies master states dictionary into local lcl_states dictionary
def init_lcl_states():
    global lcl_states
    lcl_states = dict(utilityfuncs.states)
