import sys
import utilityfuncs
import backtrack
import local

with open(sys.argv[1], "r") as statefile:
    data = statefile.readlines()

utilityfuncs.parse_input(data)
#backtrack.backtrack_search()
local.local_search()
#utilityfuncs.print_connections((local.lcl_states.values()))





