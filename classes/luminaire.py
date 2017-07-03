# classfile for theLuminaire class


class Luminaire:
    '''defines a luminaire, its position, and attributes'''

    def __init__(self, x, y, name):
        '''constructs an instance of Luminaire'''
        self.name = name
        self.position = (x, y)
        ## add other attributes here

        self.grid = None
        self.gateway = None
        self.occupancy = False;
        self.dim_lvl = 70
        self.countdown = 0 # for gradual dimming after occupancy is gone

    def set_grid(self, grid):
        '''specify the grid in which the luminaire resides'''
        self.grid = grid

    def set_gateway(self, gateway):
        '''specify the gateway to which the luminaire sends data'''
        self.gateway = gateway

    def check_occupancy(self):
        '''check if there is a person [under] the luminaire'''
        if self.grid.is_occupied(self.position): 
            self.occupancy = True
            print self.name + ' on'
        else:
            self.occupancy = False
        return self.occupancy

    def adjust_dimming(self, step):
        '''adjust dim level according to occupancy'''

        # full brightness when occupancy is true
        if self.occupancy:
            self.dim_lvl = 100
            print self.name + ' dimLvl: ' + str(self.dim_lvl)

            # push data only on first step when occupancy turns on
            if self.countdown != 30: 
                self.push_data(step)

            self.countdown = 30 # 30 ticks to gradually dim
        
        # gradual dimming
        else:
            if self.countdown == 20:
                self.dim_lvl = 90
                print self.name + ' dimLvl: ' + str(self.dim_lvl)
            elif self.countdown == 10:
                self.dim_lvl = 80
                print self.name + ' dimLvl: ' + str(self.dim_lvl)
            elif self.countdown == 0:
                self.dim_lvl = 70
            else:
                pass
            self.countdown = self.countdown-1

    def update_state(self, step):
        '''handle state changes'''
        self.check_occupancy()
        self.adjust_dimming(step)

    def get_position(self):
        '''returns co-ordinates of the luminaire as a tuple'''
        return self.position

    def push_data(self, step):
        '''pushes dictionary containg state to linked gateway'''
        state = {}
        state['timestamp'] = step
        state['name'] = self.name
        state['occupancy'] = self.occupancy
        state['dimLvl'] = self.dim_lvl
        self.gateway.store_state(state)

    # def get_state(self):
    #     '''returns attributes of the luminaire in a dictionary'''
    #     state = {}
    #     state['name'] = self.name
    #     state['occupancy'] = self.occupancy
    #     return state

