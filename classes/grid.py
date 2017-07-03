# classfile for the Grid class
from __future__ import print_function

from colorama import Fore, init

# for console coloring
init()


class Grid:
    '''defines the office space in the form of a 2D Array'''

    # origin is top left.
    # value of x determines how many steps DOWN.
    # value of y determines how many steps to the RIGHT.
    def __init__(self, width, height):
        '''constructs an instance of Grid'''

        # for console output
        self.grid = [['.' for x in range(width)] for y in range(height)]

        # for detecting occupancy
        self.occupied = [[False for x in range(width)] for y in range(height)]

        self.width = width
        self.height = height
        self.people = []
        self.luminaires = []

    def print_grid(self):
        '''outputs representation of office in ASCII format to the console'''

        # print each element of the grid in row major
        for x in range(self.height):
            for y in range(self.width):

                # colour each type of icon separately for distinguishability
                if self.grid[x][y] == 'L':
                    print(Fore.YELLOW + self.grid[x][y], end=' ')
                elif self.grid[x][y] == 'p':
                    print(Fore.MAGENTA + self.grid[x][y], end=' ')
                else:
                    print(Fore.WHITE + self.grid[x][y], end=' ')

            print('\n', end='')
        print(Fore.WHITE + '\n', end='') # clear color

    def refresh_occupancy(self):
        '''resets the occupancy grid to all False'''
        for x in range(self.height):
            for y in range(self.width):
                self.occupied[x][y] = False

    def refresh_grid(self):
        '''clears grid and adds luminaire icons'''

        # clear all 
        self.grid = [
            ['.' for x in range(self.width)] for y in range(self.height)]

        # re-add the luminaire icons
        for luminaire in self.luminaires:
            (x, y) = luminaire.get_position()
            self.grid[x][y] = 'L'

        # reset occupancy grid
        self.refresh_occupancy()

    def add_luminaire(self, luminaire):
        '''add a static luminaire to the grid'''
        self.luminaires.append(luminaire)

        # reverse link
        luminaire.set_grid(self)

        self.refresh_grid()

    def add_person(self, person):
        '''add a person to be tracked to the grid'''
        self.people.append(person)

    def track_people(self):
        '''updates the positions of the people in the grid'''
        self.refresh_grid()

        # add icon to grid at each person's position
        for person in self.people:
            (x, y) = person.get_position()

            try:
                self.grid[x][y] = 'p' # overwrites luminaire icon
            except IndexError:
                pass # gone out of the grid (can return)
            else:
                self.occupied[x][y] = True

    def is_occupied(self, position):
        '''returns true if position has person in it'''
        x = position[0]
        y = position[1]
        return self.occupied[x][y]

    def get_dimensions(self):
        '''returns height and width of the grid in a tuple'''
        return (self.height, self.width)

    # def delete_person(self, person):
    #     '''removes a person from the grid tracking'''
    #     people.remove(person)

