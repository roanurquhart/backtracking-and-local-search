import utilityfuncs
import random

backtracking_count = 0
visited = {}
bt_states = {}


def backtrack_search():
    init_bt_states()

    # Gets a random state from the list and starts the search
    random_state = random.sample(list(bt_states.values()), 1)
    random_state = random_state[0]

    print('Backtracking Search:')

    # First call to recursive backtrack search function
    if color_states(random_state):

        # Print Formatting
        for state in bt_states.values():
            print(state.get_name() + ' - ' + state.get_color())
            # Confirms there are no states that violate the rule
            utilityfuncs.no_violation(state)

        print('Nodes searched: ' + str(backtracking_count))
    else:
        print('A solution was not found')


# Recursively defined backtrack search
def color_states(state):
    increment_count()
    child_index = 0

    # Add state to visited dictionary
    visited[state.get_name()] = state

    # Island case
    if len(state.adjacentStates) == 0:
        state.set_color(state.get_available_colors()[0])
        return True

    if check_neighbor_colors(state):

        # While the node still has unvisited adjacent states
        while child_index < len(state.adjacentStates):

            state.set_color(state.get_available_colors()[0])

            # Continue to next state if current state has already been visited
            # and assigned color values that accommodate the rule
            while state.adjacentStates[child_index].get_name() in visited:
                child_index += 1
                if child_index >= len(state.adjacentStates):
                    return True

            next_state = state.adjacentStates[child_index]

            # Recursive call on next state in the adjacency list
            # If the call returns true, then we know color was successfully assigned
            # and we can proceed to next adjacent state
            if color_states(next_state):
                child_index += 1
            else:
                increment_count()
                # Eliminate the color that did not work if possible
                if len(state.colors_available) > 1:
                    state.colors_available.pop(0)
                else:
                    if state.get_name() in visited:
                        del visited[state.get_name()]
                    return False
        return True
    else:
        if state.get_name() in visited:
            del visited[state.get_name()]
        return False


# Checks the colors already being used by neighboring states
# Returns True if colors are still available and sets state's available colors
# Returns False if there are no colors available
def check_neighbor_colors(state):
    available_colors = list(utilityfuncs.colors)
    adjacent_states = state.adjacentStates

    for adj in adjacent_states:
        if adj.get_color() != 'none':
            try:
                available_colors.remove(adj.get_color())
            except:
                pass

    # If there are still valid colors, assign and return true
    # else reset color list and return false
    if len(available_colors) > 0:
        state.colors_available = available_colors
        return True
    else:
        state.colors_available = list(utilityfuncs.colors)
        return False


def increment_count():
    global backtracking_count
    backtracking_count += 1


# Copies states dictionary into local version
def init_bt_states():
    global bt_states
    bt_states = dict(utilityfuncs.states)
