import heapq

colors = []
states = {}
mrv_heap = []


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
