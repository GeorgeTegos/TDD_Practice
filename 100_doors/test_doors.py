from doors import Door
import unittest

class TestDoor(unittest.TestCase):

    def setUp(self):
        self.door_one = Door(1)

    def test_change_door_status(self):
        self.assertEqual(True,self.door_one.door_status)

if __name__=='__main__':
    unittest.main()