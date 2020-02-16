import utilityfuncs
import heapq
import random
import time

violations_heap = []
violations_list = []
possible_colors = ['Red', 'Green', 'Blue', 'Yellow']
lcl_states = {}
num_violations = 0
changes_made = 0


# Still needs work to figure out how to solve
def local_search():
    # Set up for search
    init_lcl_states()
    rand_assign()
    init_heap()

    # Variable Init
    global changes_made
    global num_violations
    global violations_list
    timeout = time.time() + 5
    count = 0

    print("Local Search:")
    print(num_violations)

    while num_violations > 0:
        # Timeout condition
        if time.time() > timeout:
            break

        # Get the next state from the violation list
        state = violations_list[0]
        if count_violations(state) == 0:
                violations_list.pop(0)
                violations_list.append(state)
                count += 1
                continue

        violations_list.pop(0)

        # Assigns color to resolve existing violations
        # May create different violations
        resolve_violations(state)

        violations_list.append(state)

    if num_violations > 0:
        print(num_violations)
        for ste in lcl_states.values():
            print(ste.get_name() + ": " + str(ste.violations))
        print(changes_made)
        print('The Local Search Timed Out - No Solution Was Found')
    else:
        for ste in lcl_states.values():
            print(ste.get_name() + ' - ' + ste.get_color())
            # Confirms there are no states that violate the rule
            utilityfuncs.no_violation(ste)
        #utilityfuncs.print_connections(lcl_states.values())
        print('Changes made: ' + str(changes_made))


# Randomly assigns a color value to all of the states
def rand_assign():
    for state in lcl_states.values():
        random_color = random.sample(state.colors_available, 1)
        state.set_color(random_color[0])


# Sets a color to the state based on the least used color in the
# adjacent states
def resolve_violations(loc):
    # Variable Initialization
    global changes_made
    global num_violations
    adj_color_count = {"Red": 0, "Blue": 0, "Green": 0, "Yellow": 0}
    available_colors = list(utilityfuncs.colors)

    # Counts the number of each color in surrounding states
    # and filters a list of colors, which if
    # assigned would cause no violation
    for adj in loc.adjacentStates:
        try:
            adj_color_count[adj.get_color()] += 1
            available_colors.remove(adj.get_color())
        except:
            pass

    # If colors are available, assign
    if len(available_colors) != 0:
        loc.set_color(available_colors[0])
        num_violations -= loc.violations * 2
        loc.violations = 0
        changes_made += 1
    else:
        # Set the color to the least used color in order
        # to fix the most violations
        minimum = 1000000
        min_color = ''
        for color in adj_color_count.keys():
            if adj_color_count[color] < minimum:
                minimum = adj_color_count[color]
                min_color = color
        num_violations -= (loc.violations * 2) - (minimum * 2)
        loc.violations = minimum
        loc.set_color(min_color)
        changes_made += 1


# Creates the heap that orders the states by amount of violations
def init_heap():
    global num_violations
    for state in lcl_states.values():
        violations = count_violations(state)
        # Negate values in order to create max heap, need to abs value values later
        heapq.heappush(violations_heap, ((-1 * violations), state.get_name()))
        num_violations += violations
    simplify_copy_heap()


# Copies heap into list form to simplify violation resolution
def simplify_copy_heap():
    global violations_list
    while len(violations_heap) > 0:
        state = heapq.heappop(violations_heap)
        violations_list.append(lcl_states[state[1]])


# Prints the violations heap, but depopulates
def print_heap():
    while len(violations_heap) > 0:
        state = heapq.heappop(violations_heap)
        print(state[1] + ": " + str(state[0]))


# Counts the number of violations a state has after randomization
def count_violations(state):
    count = 0

    for ste in state.adjacentStates:
        if state.get_color() == ste.get_color():
            count += 1

    state.violations = count
    return count


# Copies master states dictionary into local lcl_states dictionary
def init_lcl_states():
    global lcl_states
    lcl_states = dict(utilityfuncs.states)
