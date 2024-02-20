import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_str(self):
        s = Square(5, 3, 4, 1)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 5")

    def test_size(self):
        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 20
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_update(self):
        s = Square(5, 3, 4, 1)
        s.update(2)
        self.assertEqual(str(s), "[Square] (2) 3/4 - 5")
        s.update(3, 10)
        self.assertEqual(str(s), "[Square] (3) 3/4 - 10")
        s.update(4, 10, 5)
        self.assertEqual(str(s), "[Square] (4) 5/4 - 10")
        s.update(5, 10, 5, 2)
        self.assertEqual(str(s), "[Square] (5) 5/2 - 10")

    def test_to_dictionary(self):
        s = Square(5, 3, 4, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 1, 'size': 5, 'x': 3, 'y': 4})
