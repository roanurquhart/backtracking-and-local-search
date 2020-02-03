import random
import heapq

colors = []
states = {}
mrv_heap = []
visited = {}

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
        #conns = len(st.adjacentStates)
        heapq.heappush(mrv_heap, (conns, st.get_name()))

    while len(mrv_heap) != 0:
        ste = heapq.heappop(mrv_heap)
        print(ste[1] + ' ' + str(ste[0]))


def backtrack_search():
    # Put in some optimization discussed in class - Probably Most Constrained Variable

    # Right now this just gets a random state from the list and starts the search
    random_state = random.sample(list(states.values()), 1)
    random_state = random_state[0]
    if color_states(random_state):
        for state in states.values():
            print(state.get_name() + ' - ' + state.get_color())
    else:
        print('A solution was not found')


# Basic recursively defined backtrack search
def color_states(state):
    child_index = 0
    visited[state.get_name()] = state
    if check_neighbor_colors(state):
        while child_index < len(state.adjacentStates):
            state.set_color(state.get_available_colors()[0])
            while state.adjacentStates[child_index].get_name() in visited:
                child_index += 1
                if child_index >= len(state.adjacentStates):
                    return True
            next_state = state.adjacentStates[child_index]
            if color_states(next_state):
                child_index += 1
            else:
                if len(state.colors_available) > 1:
                    state.colors_available.pop(0)
                else:
                    return False
        return True
    else:
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


def print_connections(locations):
    for location in locations:
        print(location.get_name())
        adjacent_locations = location.adjacentStates
        print('{', end='')
        for loc in adjacent_locations:
            print(loc.get_name() + ',', end='')
        print('}')
