# classfile for the Grid class
from __future__ import print_function

class Grid:
    '''defines the office space in the form of a 2D Array'''

    # default grid is 10x10, pass width and height when instantiating to 
    # override this behavior
    def __init__(self, width=10, height=10):
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
                print(self.grid[x][y], end=' ')
            print('\n', end='')

    def refresh_occupancy(self):
        '''resets the occupancy grid to all False'''
        for x in range(self.height):
            for y in range(self.width):
                self.occupied[x][y] = False

    def refresh_grid(self):
        '''clears grid and adds luminaire icons'''

        # clear all 
        self.grid = [['.' for x in range(width)] for y in range(height)]

        # re-add the luminaire icons
        for luminaire in self.luminaires:
            (x, y) = luminaire.get_position() ## will it work without import?
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
            (x, y) = person.get_position() ## will it work without import?
            self.grid[x][y] = 'p' ## this will overwrite the luminaire icon
            self.occupied[x][y] = True

    def is_occupied(self, position):
        '''returns true if position has person in it'''
        x = position[0]
        y = position[1]
        return self.occupied[x][y]

