class Door:

    def __init__(self,door_number,door_status=False):
        self.door_status = door_status
        self.door_number = door_number

    def change_door_status(self):
        if self.door_status == False:
            self.door_status = True
            return self.door_status
        else:
            self.door_status = False
            return self.door_status
        