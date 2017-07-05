# classfile for the Luminaire class
from multiprocessing import Queue
import thread


class Luminaire:
    '''defines a luminaire, its position, and attributes'''

    def __init__(self, x, y, name):
        '''constructs an instance of Luminaire'''
        self.name = name
        self.position = (x, y)

        self.source = 'grid'
        self.bat_charging = 'grid'
        self.event_queue = Queue()
        self.thread_alive = False

        self.grid = None
        self.gateway = None
        self.occupancy = False
        self.dim_lvl = 70
        self.countdown = 0 # for gradual dimming after occupancy is gone

        self.lum_address = None
        self.bib_mode = None
        self.pir_status = None
        self.bat_state = None
        self.bat_soc = None
        self.xsr_power = None
        self.led_power = None
        self.bat_power = None
        self.lum_op_mode = None
        self.faults = None
        self.bright_level = None

        thread.start_new_thread(self.luminaire_thread, ())

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

    def check_thread(self):
        '''checks if thread is still alive'''
        if self.thread_alive:
            self.thread_alive = False
            return True
        else:
            return False


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

    def add_event_to_queue(self, event):
        '''adds an event to be processed in the queue'''
        self.event_queue.put(event)

    def luminaire_thread(self):
        '''makes adjustments according to events'''
        while True:
            self.thread_alive = True
            try:

                # check for events in the queue and process them
                if not self.event_queue.empty():
                    event = self.event_queue.get()
                    
                    if event == 'source-grid':
                        self.source = 'grid'
                    elif event == 'source-battery':
                        self.source = 'battery'
                    elif event == 'charging-grid':
                        self.bat_charging = 'grid'
                    elif event == 'charging-solar':
                        self.bat_charging = 'solar'
                    else:
                        pass

            except IOError:
                pass

    # def set_source(self, source):
    #     '''specify source of power for the luminaire'''
    #     self.source = source

    # def set_bat_charging(self, charging_source):
    #     '''specify source from which battery should charge'''
    #     self.bat_charging = charging_source

    # def get_state(self):
    #     '''returns attributes of the luminaire in a dictionary'''
    #     state = {}
    #     state['name'] = self.name
    #     state['occupancy'] = self.occupancy
    #     return state

