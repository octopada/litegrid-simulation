# main file creates all the entities and runs the simulation
from random import randint
from time import sleep

from classes import grid, luminaire, person, gateway

# global vars
PEOPLE_COUNT = 5
STEP_COUNT = 10

# construct grid
grid = grid.Grid()

# construct gateway
gateway = gateway.Gateway()

# construct luminaires
lum_no = 0
luminaires = []

    # arbitrary grid of luminaires
for x in range(1, 10, 2):
    for y in range(1, 10, 2):
        lum_name = 'lum'+str(lum_no)
        lum = luminaire.Luminaire(x, y, lum_name)
        luminaires.append(lum)
        lum_no = lum_no+1

# construct people
people = []

    # place them randomly
count = 0
while count != PEOPLE_COUNT:
    person_instance = person.Person(randint(0, 10), randint(0, 10))
    people.append(person_instance)
    count = count+1

# add luminaires to grid, gateway
for luminaire in luminaires:
    grid.add_luminaire(luminaire)
    gateway.add_luminaire(luminaire)

# add people to grid
for person in people:
    grid.add_person(person)
grid.track_people()

# initial print
grid.print_grid()

# run simulation for given no of steps
for step in range(STEP_COUNT):

    # pause for visualization
    sleep(2)

    # move people
    for person in people:
        person.random_move()

    # track people in grid
    grid.track_people()

    # check occupancy
    for luminaire in luminaires:
        luminaire.check_occupancy()

    # gateway collects data, using step as timestamp
    gateway.get_state_data(step)

    # show grid
    grid.print_grid()

    for person in people:
        (x, y) = person.get_position()
        print x, y

# output
gateway.publish_state_data()