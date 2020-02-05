import sys
import utilityfuncs

with open(sys.argv[1], "r") as statefile:
    data = statefile.readlines()

utilityfuncs.parse_input(data)
utilityfuncs.backtrack_search()
#utilityfuncs.print_connections((utilityfuncs.states.values()))





