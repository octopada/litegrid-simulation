# main file creates all the entities and runs the simulation
from time import sleep

from classes import grid, luminaire, person, gateway

# construct grid
grid = grid.Grid()

# construct gateway
gateway = gateway.Gateway()

# construct luminaires
luminaires = []
lum = luminaire.Luminaire(5, 5, 'lum1')
luminaires.append(lum)

# construct people
people = []
person = person.Person(5, 0)
people.append(person)

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

time = -1
quit = False
while not quit:

    # for timestamps
    time = time+1

    # move people
    for person in people:
        quit = person.controlled_move()

    # track people in grid
    grid.track_people()

    # check occupancy
    for luminaire in luminaires:
        luminaire.check_occupancy()

    # gateway collects data
    gateway.get_state_data(time)

    # show grid
    grid.print_grid()

    # wait a bit before next step
    # sleep(0.5)

# output
gateway.publish_state_data()