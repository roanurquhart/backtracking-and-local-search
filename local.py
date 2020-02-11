import utilityfuncs
import heapq
import random
import time

violations_heap = []
lcl_states = {}
num_violations = 0
changes_made = 0


# Still needs work to figure out how to solve
def local_search():
    init_lcl_states()
    rand_assign()
    init_heap()
    global changes_made
    global num_violations
    timeout = time.time() + 15
    repeater = ''
    count = 0
    print("Local Search:")
    print(violations_heap[0])
    while len(violations_heap) != 0:
        state_tuple = heapq.heappop(violations_heap)
        state = lcl_states[state_tuple[1]]
        # To stop a state from causing an infinite loop
        if repeater == state:
            count += 1
            if count > 10:
                break
        else:
            count = 0
        repeater = state
        print(state_tuple)
        resolve_violations(state)
        violations_remain = count_violations(state)
        print(violations_remain)
        num_violations += violations_remain - state_tuple[0]
        if violations_remain != 0:
            heapq.heappush(violations_heap, ((-1 * violations_remain), state.get_name()))
        if time.time() > timeout:
            break
        count += 1
    if len(violations_heap) != 0:
        print(len(violations_heap))
        print('The Local Search Timed Out - No Solution Was Found')
    else:
        for ste in lcl_states.values():
            print(ste.get_name() + ' - ' + ste.get_color())
            # Confirms there are no states that violate the rule
            utilityfuncs.no_violation(ste)
        utilityfuncs.print_connections(lcl_states.values())
        print('Changes made: ' + str(changes_made))


# Randomly assigns a color value to all of the states
def rand_assign():
    for state in lcl_states.values():
        random_color = random.sample(state.colors_available, 1)
        state.set_color(random_color[0])


def resolve_violations(state):
    adj_color_count = {"Red": 0, "Blue": 0, "Green": 0, "Yellow": 0}
    available_colors = list(utilityfuncs.colors)
    for adj in state.adjacentStates:
        try:
            adj_color_count[adj.get_color()] += 1
            available_colors.remove(adj.get_color())
        except:
            pass
    if len(available_colors) != 0:
        state.set_color(available_colors[0])
        global changes_made
        changes_made += 1
    else:
        # Set the color to the least used color in order to fix the most violations
        minimum = 1000000
        min_color = ''
        for color in adj_color_count.keys():
            if adj_color_count[color] < minimum:
                minimum = adj_color_count[color]
                min_color = color
        state.set_color(min_color)


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
