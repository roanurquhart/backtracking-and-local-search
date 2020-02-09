import sys
import utilityfuncs
import backtrack

with open(sys.argv[1], "r") as statefile:
    data = statefile.readlines()

utilityfuncs.parse_input(data)
backtrack.backtrack_search()
#utilityfuncs.print_connections((utilityfuncs.states.values()))





