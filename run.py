import nxbt

macro = """
B 0.1s
0.1s
"""

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

# Run a macro on the Pro Controller
nx.macro(controller_index, macro)