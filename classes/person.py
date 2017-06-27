# classfile for the Person class


class Person:
    '''defines a person, their position and movement'''

    def __init__(self, x, y):
        '''constructs an instance of Person'''
        self.position = (x, y)

    def move(self):
        '''changes position'''
        x = self.position[0]
        y = self.position[1]
        y = y+1 ## [one step right]
        self.position = (x, y)

