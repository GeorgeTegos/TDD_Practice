from door import Door

class Doors:

    def __init__(self):
        self.doors_list = []
    
    def add_door_to_doors_list(self,door):
        self.doors_list.append(door)

    def populate_doors_with_door_object(self,list_of_door_objects):
        for door in list_of_door_objects:
            self.add_door_to_doors_list(door)


    def iterate_and_change_door_status_by_step(self,step = 1):
        while step <= len(self.doors_list):
            for i in range(0,len(self.doors_list),step):
                self.doors_list[i-1].change_door_status()
            step += 1
                

    

