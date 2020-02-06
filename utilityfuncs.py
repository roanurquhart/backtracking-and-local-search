import random
import heapq

colors = []
states = {}
mrv_heap = []
visited = {}
backtracking_count = 0


class State:
    def __init__(self, name):
        self.name = name
        self.adjacentStates = []
        self.color = 'none'
        self.colors_available = list(colors)

    def __repr__(self):
        return "<State name:%s adjacentStates:%s>" % (self.name, self.adjacentStates)

    def __str__(self):
        return "Test: name:%s, adjacentStates:%s" % (self.name, self.adjacentStates)

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_available_colors(self):
        return self.colors_available


def parse_input(data):
    input_increment = 0
    counter = 0
    while input_increment < 3:
        while input_increment == 0:
            if data[counter] != '\n':
                colors.append(data[counter].rstrip())
                counter += 1
            else:
                counter += 1
                input_increment += 1
        while input_increment == 1:
            if data[counter] != '\n':
                state_name = data[counter].rstrip()
                state = State(state_name)
                states[state_name] = state
                counter += 1
            else:
                counter += 1
                input_increment += 1
        while input_increment == 2:
            if counter < len(data):
                connection = data[counter].split()
                state_one = states[connection[0]]
                state_two = states[connection[1]]
                state_one.adjacentStates.append(state_two)
                state_two.adjacentStates.append(state_one)
                counter += 1
            else:
                counter += 1
                input_increment += 1


def init_heap():
    for st in states.values():
        conns = len(st.get_available_colors())
        heapq.heappush(mrv_heap, (conns, st.get_name()))


def backtrack_search():
    # Put in some optimization discussed in class - Probably Most Constrained Variable

    # Right now this just gets a random state from the list and starts the search
    random_state = random.sample(list(states.values()), 1)
    random_state = random_state[0]
    if color_states(random_state):
        for state in states.values():
            print(state.get_name() + ' - ' + state.get_color())
            no_violation(state)
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

    if check_neighbor_colors(state):
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


# Checks the colors already being used by neighboring states
# Returns True if colors are still available and sets state's available colors
# Returns False if there are no colors available
def check_neighbor_colors(state):
    available_colors = list(colors)
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
        state.colors_available = list(colors)
        return False


# Counts the connected states that have not been assigned colors
def states_without_color(state_list):
    counter = 0
    for ste in state_list:
        if ste.get_color() == 'none':
            counter += 1

    return counter


# Checks each state for violation of rule
def no_violation(state):
    state_color = state.get_color()
    for ste in state.adjacentStates:
        if state_color == ste.get_color():
            print('breaks')
            return
    return


def print_connections(locations):
    for location in locations:
        print(location.get_name() + ': ' + location.get_color())
        adjacent_locations = location.adjacentStates
        print('{', end='')
        for loc in adjacent_locations:
            print(loc.get_name() + ': ' + loc.get_color() + ',', end='')
        print('}')
