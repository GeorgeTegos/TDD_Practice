from door import Door
from doors import Doors
import unittest

class TestDoor(unittest.TestCase):

    def setUp(self):
        self.door_one = Door(1,False)
        self.doors = Doors()

    def test_change_door_status(self):
        self.assertEqual(True,self.door_one.change_door_status())

    def test_add_door_to_doors(self):
        self.assertEqual(1,len(self.doors.doors_list))



if __name__=='__main__':
    unittest.main()