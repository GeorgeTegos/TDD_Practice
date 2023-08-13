from door import Door
from doors import Doors
from runner import create_100_doors
import unittest

class TestDoor(unittest.TestCase):

    def setUp(self):
        self.door_one = Door(1,False)
        self.doors = Doors()

    def test_change_door_status(self):
        self.assertEqual(True,self.door_one.change_door_status())

    def test_add_door_to_doors_list(self):
        self.doors.add_door_to_doors_list(self.door_one)
        self.assertEqual(1,len(self.doors.doors_list))

    def test_create_100_doors(self):
        self.assertEqual(100,len(create_100_doors()))

    def test_populate_doors_with_door_objects(self):
        list_of_door_objects = create_100_doors()
        self.doors.populate_doors_with_door_object(list_of_door_objects)
        self.assertEqual(100,len(self.doors.doors_list))

if __name__=='__main__':
    unittest.main()