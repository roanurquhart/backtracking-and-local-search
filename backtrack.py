import utilityfuncs
import random

backtracking_count = 0
visited = {}


def backtrack_search():
    # Gets a random state from the list and starts the search
    random_state = random.sample(list(utilityfuncs.states.values()), 1)
    random_state = random_state[0]
    # First call to recursive backtrack search function
    if color_states(random_state):
        # Print Formatting
        for state in utilityfuncs.states.values():
            print(state.get_name() + ' - ' + state.get_color())
            # Confirms there are no states that violate the rule
            utilityfuncs.no_violation(state)
        print('Nodes searched: ' + str(backtracking_count))
    else:
        print('A solution was not found')


# Recursively defined backtrack search
def color_states(state):
    global backtracking_count
    backtracking_count += 1
    child_index = 0
    visited[state.get_name()] = state

    # Island case
    if len(state.adjacentStates) == 0:
        state.set_color(state.get_available_colors()[0])
        return True

    if utilityfuncs.check_neighbor_colors(state):
        # While the node still has unvisited adjacent states
        while child_index < len(state.adjacentStates):
            state.set_color(state.get_available_colors()[0])
            # In case some adjacent states have already been visited
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
