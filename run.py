import nxbt


'''
macro_getOutOfMenu = """
A 0.1s
2s
B 0.1s
2s
DPAD_UP 0.1s
2s
DPAD_LEFT 0.1s
2s
DPAD_LEFT 0.1s
2s
A 0.1s
2s
"""

macro_LoopA = """
LOOP 100000
    A 0.1s
    0.5s
"""
'''

macro = """
A 0.1s
5s
B 0.1s
5s
DPAD_UP 0.1s
2s
DPAD_LEFT 0.1s
2s
DPAD_LEFT 0.1s
2s
A 0.1s
2s
LOOP 100000
    R 0.1s
    0.1s
    A 0.1s
    0.5s
"""

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)
print("connected");
nx.macro(controller_index, macro)

# Run a macro on the Pro Controller
# nx.macro(controller_index, macro_getOutOfMenu)
# Loop A
# nx.macro(controller_index, macro_LoopA)
# Make a python loop where if you press enter it stops looping?