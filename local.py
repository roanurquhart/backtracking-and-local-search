import utilityfuncs
import heapq
import random

violations_heap = []
lcl_states = {}


def local_search():
    init_lcl_states()
    init_heap()


def rand_assign():
    hello = 0


def init_heap():
    for st in utilityfuncs.states.values():
        conns = len(st.get_available_colors())
        heapq.heappush(violations_heap, (conns, st.get_name()))


def init_lcl_states():
    global lcl_states
    lcl_states = dict(utilityfuncs.states)
