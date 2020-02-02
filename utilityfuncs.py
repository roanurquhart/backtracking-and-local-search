
colors = []
states = {}

class State:
    def __init__(self, name):
        self.name = name
        self.adjacentStates = []

    def __repr__(self):
        return "<State name:%s adjacentStates:%s>" % (self.name, self.adjacentStates)

    def __str__(self):
        return "Test: name:%s, adjacentStates:%s" % (self.name, self.adjacentStates)

    def get_name(self):
        return self.name


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


def print_connections(states):
    for location in states:
        print(location.name)
        a = location.adjacentStates
        print('{', end='')
        for loc in a:
            print(loc.get_name() + ',', end='')
        print('}')