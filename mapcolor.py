import sys
import utilityfuncs

with open(sys.argv[1], "r") as ausfile:
    data = ausfile.readlines()
    print(data)


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


inputIncrement = 0
counter = 0
colors = []
states = {}
while inputIncrement < 3:
    while inputIncrement == 0:
        if data[counter] != '\n':
            colors.append(data[counter].rstrip())
            counter += 1
        else:
            counter += 1
            inputIncrement += 1
    while inputIncrement == 1:
        if data[counter] != '\n':
            stateName = data[counter].rstrip()
            state = State(stateName)
            states[stateName] = state
            counter += 1
        else:
            counter += 1
            inputIncrement += 1
    while inputIncrement == 2:
        if counter < len(data):
            connection = data[counter].split()
            stateOne = states[connection[0]]
            stateTwo = states[connection[1]]
            stateOne.adjacentStates.append(stateTwo)
            stateTwo.adjacentStates.append(stateOne)
            counter += 1
        else:
            counter += 1
            inputIncrement += 1

utilityfuncs.print_connections((states.values()))





