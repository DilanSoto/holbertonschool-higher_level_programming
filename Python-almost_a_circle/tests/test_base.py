import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base__init__(self):
        """Test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_create(self, **dictionary):
        """Test the create method of the Base class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)
        # self.assertEqual(r1, r2)

        self.assertIsNot(r1, r2)

    def test_save_to_file(self):
        """Test the save_to_file method of the Base class"""
        # # save and load a list of retangles
        # r1 = Rectangle(10, 7, 2, 8)
        # r2 = Rectangle(2, 4)
        # list_rectangles_input = [r1, r2]

        # Rectangle.save_to_file(list_rectangles_input)
        # list_rectangles_output = Rectangle.load_from_file()

        # self.assertEqual(list_rectangles_input, list_rectangles_output)

        # # save and load a list of Square instances
        # s1 = Square(5)
        # s2 = Square(7, 9, 1)
        # list_squares_input = [s1, s2]

        # Square .save_to_file(list_squares_input)
        # list_squares_output = Square.load_from_file()

        # self.assertEqual(list_squares_input, list_squares_output)

    # def test_load_from_file(cls):


if __name__ == '__main__':
    unittest.main()
