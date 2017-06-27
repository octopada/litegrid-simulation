# classfile for Luminaire class


class Luminaire:
    '''defines a luminaire, its position, and attributes'''

    def __init__(self, x, y):
        '''constructs an instance of Luminaire'''
        self.grid = None
        self.position = (x, y)
        self.occupancy = False;
        # add other attributes here

    def set_grid(self, grid):
        '''specify the grid in which the luminaire resides'''
        self.grid = grid

    def check_occupancy(self):
        '''check if there is a person [under] the luminaire'''
        if self.grid.is_occupied(position):
            self.occupancy = True
        else:
            self.occupancy = False

    def get_state(self):
        '''returns attributes of the luminaire in a dictionary'''
        state = {}
        state['occupancy'] = self.occupancy
        return state

    def get_position(self):
        '''returns co-ordinates of the luminaire as a tuple'''
        return self.position

