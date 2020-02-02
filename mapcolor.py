import sys

with open(sys.argv[1], "r") as ausfile:
    data = ausfile.readlines()
    print(data)


class State:
    def __init__(self, name):
        self.name = name
        self.adjacentStates = []


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
            print(states)
    while inputIncrement == 2:
        if counter < len(data):
            connection = State(data[counter].split())
            states[connection[0]].adjacentStates.append(connection[1])
            counter += 1
        else:
            counter += 1
            inputIncrement += 1



