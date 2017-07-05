# classfile for the Person class
from msvcrt import getch
from random import randint


class Person:
    '''defines a person, their position and movement'''

    def __init__(self, x, y):
        '''constructs an instance of Person'''
        self.position = (x, y)
        self.grid = None

    def controlled_move(self):
        '''changes position according to input'''
        quit = False

        x = self.position[0]
        y = self.position[1]

        (lower_bound, right_bound) = self.grid.get_dimensions()

        print 'Press WASD to move person, X to quit'
        input_char = getch()

        if input_char.upper() == 'W':
            if x != 0:
                x = x-1
        elif input_char.upper() == 'A':
            if y != 0:
                y = y-1
        elif input_char.upper() == 'S':
            if x != lower_bound-1:
                x = x+1
        elif input_char.upper() == 'D':
            if y != right_bound-1:
                y = y+1
        elif input_char.upper() == 'X':
            quit = True
        else:
            pass

        self.position = (x, y)

        return quit

    # people are able to move out of the grid
    def random_move(self):
        '''changes position in random direction'''
        x = self.position[0]
        y = self.position[1]

        (lower_bound, right_bound) = self.grid.get_dimensions()

        # 1 - UP
        # 2 - LEFT
        # 3 - DOWN
        # 4 - RIGHT
        direction = randint(1, 4)

        if direction == 1:
            if x != 0:
                x = x-1
        elif direction == 2:
            if y != 0:
                y = y-1
        elif direction == 3:
            if x != lower_bound-1:
                x = x+1
        elif direction == 4:
            if y != right_bound-1:
                y = y+1

        self.position = (x, y)

    def get_position(self):
        '''returns co-ordinates of the person as a tuple'''
        return self.position

    def set_grid(self, grid):
        '''specify the grid in which the person resides'''
        self.grid = grid

