# classfile for class Simulator that runs the simulation
from msvcrt import getch, kbhit
from random import randint
from time import sleep

from classes.grid import Grid 
from classes.luminaire import Luminaire 
from classes.person import Person 
from classes.gateway import Gateway


class Simulator:
    '''singleton class that will run the simulation'''

    @classmethod
    def setup(cls, people_count, grid_width, grid_height):
        '''constructs an instance of Simulator'''

        # construct grid and gateway
        cls.grid = Grid(grid_width, grid_height)
        cls.gateway = Gateway()

        # construct arbitrary luminaire grid
        cls.luminaires = []
        (grid_height, grid_width) = cls.grid.get_dimensions()

        lum_no = 0
        for x in range(1, grid_height-1, 2):
            for y in range(1, grid_width-1, 2):

                # generate name for the luminaire
                lum_name = 'lum' + str(lum_no)

                lum = Luminaire(x, y, lum_name)
                cls.luminaires.append(lum)
                lum_no = lum_no+1

        # construct people and place them randomly
        cls.people = []
        for count in range(people_count):
            person_x = randint(0, grid_height-1)
            person_y = randint(0, grid_width-1)
            person = Person(person_x, person_y)
            cls.people.append(person)

        # add luminaires to grid, gateway
        for luminaire in cls.luminaires:
            cls.grid.add_luminaire(luminaire)
            cls.gateway.add_luminaire(luminaire)

        # add people to grid
        for person in cls.people:
            cls.grid.add_person(person)
        cls.grid.track_people()

    # pass user_prompt as True to get 'press to continue' functionality
    # default behavior is 0.5 second sleep
    @classmethod
    def run_random(cls, step_count, user_prompt=False):
        '''run simulation with random person movement for given steps'''
        sleep_time = 0.5
        for step in range(step_count):

            print 'step ' + str(step)

            # movement every 4 ticks
            if step%4 == 0:

                # show grid
                cls.grid.print_grid()

                # move people
                for person in cls.people:
                    person.random_move()

                # track people in grid
                cls.grid.track_people()

            # update luminaire states
            for luminaire in cls.luminaires:
                luminaire.update_state(step)

            # luminaires push data every 10 ticks, using step as timestamp
            if step%10 == 0:
                for luminaire in cls.luminaires:
                    luminaire.push_data(step)

            # pause for visualization
            wait = True
            if user_prompt:
                print 'press S for next step'
                while wait:
                    if kbhit():
                        wait = False

                # clear keyboard buffer
                while kbhit():
                    getch()
            else:    
                sleep(sleep_time)

        # output
        cls.gateway.publish_state_data()

    # waits for user input before every step, quits on user command
    @classmethod
    def run_controlled(cls):
        '''run simulation with controlled person movement'''
        quit = False
        step = 0
        while not quit:

            print 'step ' + str(step) 

            # move and track people every 4 ticks
            if step%4 == 0:

                # show grid
                cls.grid.print_grid()

                for person in cls.people:
                    quit = person.controlled_move()
                    cls.grid.track_people()

            # update luminaire states
            for luminaire in cls.luminaires:
                luminaire.update_state(step)

            # luminaires push data every 10 ticks, using step as timestamp
            if step%10 == 0:
                for luminaire in cls.luminaires:
                    luminaire.push_data(step)
            step = step+1

        # output
        cls.gateway.publish_state_data()

