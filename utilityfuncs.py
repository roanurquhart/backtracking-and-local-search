

def print_connections(states):
    for location in states:
        print(location.name)
        a = location.adjacentStates
        print('{', end='')
        for loc in a:
            print(loc.get_name() + ',', end='')
        print('}')