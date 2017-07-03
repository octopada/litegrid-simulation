# main
from msvcrt import getch

from classes.simulator import Simulator

# globals
PEOPLE_COUNT_RANDOM = 5
PEOPLE_COUNT_CONTROLLED = 1 # multiple persons will have to moved one by one
STEP_COUNT = 50
USER_PROMPT = False # change to true to disable sleep timer in random mode
GRID_WIDTH = 11
GRID_HEIGHT = 11

# menu
print '1. Random Person Movement'
print '2. Controlled Person Movement'
print 'Enter choice'

# process input and run simulator accordingly
input_char = getch()
if input_char == '1':
    Simulator.setup(PEOPLE_COUNT_RANDOM, GRID_WIDTH, GRID_HEIGHT)
    Simulator.run_random(STEP_COUNT, USER_PROMPT)
elif input_char == '2':
    Simulator.setup(PEOPLE_COUNT_CONTROLLED, GRID_WIDTH, GRID_HEIGHT)
    Simulator.run_controlled()
else:
    print 'You have not chosen well.'