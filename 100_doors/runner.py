from door import Door
from doors import Doors

doors = Doors()

def create_100_doors():
    local_list = []
    for door_number in range(1,101):
        door = Door(door_number)
        local_list.append(door)
    return local_list

