# classfile for the Grid class
from __future__ import print_function


class Grid:
    ''' defines the office space in the form a 2D Array '''

    # default grid is 10x10, pass width and height when instantiating to 
    # override this behavior
    def __init__(self, width=10, height=10):
        ''' constructs an instance of Grid '''
        self.grid = [['.' for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height

    def print_grid(self):
        ''' outputs representation of office in ASCII format to the console '''

        # print each element of the grid in row major
        for x in range(self.height):
            for y in range(self.width):
                print(self.grid[x][y], end=' ')
            print('\n', end='')

