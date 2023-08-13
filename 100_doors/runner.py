from door import Door
from doors import Doors

doors = Doors()

def create_100_doors():
    list_of_door_objects = []
    for door_number in range(1,101):
        door = Door(door_number)
        list_of_door_objects.append(door)
    return list_of_door_objects




