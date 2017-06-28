# classfile for the Person class
from msvcrt import getch


class Person:
    '''defines a person, their position and movement'''

    def __init__(self, x, y):
        '''constructs an instance of Person'''
        self.position = (x, y)

    def controlled_move(self):
        '''changes position'''
        quit = False

        x = self.position[0]
        y = self.position[1]

        print 'Press WASD to move person'
        input_char = getch()

        if input_char.upper() == 'W':
            x = x-1
        elif input_char.upper() == 'A':
            y = y-1
        elif input_char.upper() == 'S':
            x = x+1
        elif input_char.upper() == 'D':
            y = y+1
        elif input_char.upper() == 'X':
            quit = True
        else:
            pass

        self.position = (x, y)

        return quit

    def get_position(self):
        '''returns co-ordinates of the person as a tuple'''
        return self.position

