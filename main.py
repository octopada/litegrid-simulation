# main
from msvcrt import getch

from classes.simulator import Simulator

# globals
PEOPLE_COUNT_RANDOM = 5
PEOPLE_COUNT_CONTROLLED = 1 # multiple persons will have to moved one by one
STEP_COUNT = 50
USER_PROMPT = False # change to true to disable sleep timer in random mode
GRID_WIDTH = 5 # best to keep it odd, the arbitrary luminaire grid fits well
GRID_HEIGHT = 5 # same as above

# menu
print '1. Random Person Movement'
print '2. Controlled Person Movement'
print 'Enter choice'

# process input and run simulator accordingly
input_char = getch()

# random mode
if input_char == '1':
    Simulator.setup(PEOPLE_COUNT_RANDOM, GRID_WIDTH, GRID_HEIGHT)
    Simulator.run_random(STEP_COUNT, USER_PROMPT)

# controlled mode
elif input_char == '2':
    Simulator.setup(PEOPLE_COUNT_CONTROLLED, GRID_WIDTH, GRID_HEIGHT)
    Simulator.run_controlled()
    
else:
    print 'You have not chosen well.'