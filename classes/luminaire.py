# classfile for theLuminaire class


class Luminaire:
    '''defines a luminaire, its position, and attributes'''

    def __init__(self, x, y, name):
        '''constructs an instance of Luminaire'''
        self.name = name
        self.position = (x, y)
        ## add other attributes here

        self.grid = None
        self.occupancy = False;

    def set_grid(self, grid):
        '''specify the grid in which the luminaire resides'''
        self.grid = grid

    def check_occupancy(self):
        '''check if there is a person [under] the luminaire'''
        if self.grid.is_occupied(position): ## will it work without import?
            self.occupancy = True
        else:
            self.occupancy = False

    def get_state(self):
        '''returns attributes of the luminaire in a dictionary'''
        state = {}
        state['name'] = self.name
        state['occupancy'] = self.occupancy
        return state

    def get_position(self):
        '''returns co-ordinates of the luminaire as a tuple'''
        return self.position

