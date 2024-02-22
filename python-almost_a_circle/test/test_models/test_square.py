from models.square import Square
import unittest


class TestSquare(unittest.TestCase):

    """ Checker preference """
    def test_checker(self):
        with self.assertRaises(ValueError):
            sqr = Square(0)

    """ Testing id """
    def test_id(self):
        sqr = Square(1)
        self.assertAlmostEqual(sqr.id, 35)

    """ Testing size """
    def test_size(self):
        sqr = Square(1, 2)
        self.assertEqual(sqr.size, 1)

    """ Testing width """
    def test_width(self):
        sqr = Square(1, 2, 3)
        self.assertEqual(sqr.width, 1)

    """ Testing a str as argument """
    def test_str_1_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square("1")

    def test_str_2_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square(1, "2")

    def test_str_3_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square(1, 2, "3")

    """ Testing Negative Arguments """
    def test_neg_arg_1(self):
        with self.assertRaises(ValueError):
            sqr = Square(-1)

    def test_neg_arg_2(self):
        with self.assertRaises(ValueError):
            sqr = Square(1, -2)

    def test_neg_arg_3(self):
        with self.assertRaises(ValueError):
            sqr = Square(1, 2, -3)

    """ Testing __str__ method """
    def test_str_method(self):
        sqr = Square(5)
        self.assertEqual(sqr.__str__(), "[Square] (48) 0/0 - 5")

    """ Testing to_dictionary method """
    def test_to_dic(self):
        sqr = Square(10, 2, 1, 6)
        result = {'id': 6, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(sqr.to_dictionary(), result)

    """ Testing update method """
    def test_update(self):
        sqr = Square(5)
        sqr.update(10)
        self.assertEqual(sqr.id, 10)
        sqr.update(1, 2)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.width, 2)
        sqr.update(1, 2, 3)
        self.assertEqual(sqr.x, 3)
        sqr.update(1, 2, 3, 4)
        self.assertEqual(sqr.y, 4)

    """ Testing create method """
    def test_create(self):
        sqr1 = Square(2)
        sqr1_dic = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dic)
        self.assertNotEqual(sqr1, sqr2)

    """ Testing to save to file """
    def test_save_to_file_empty(self):
        Square.save_to_file(None)
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file_empty_2(self):
        Square.save_to_file([])
        with open("Square.json") as fd:
            self.assertEqual('[]', fd.read())

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])
        result = '[{"id": 43, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json") as fd:
            self.assertEqual(result, fd.read())

    """ Test load from file """
    def test_load_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        li_sqr_out = Square.load_from_file()
        self.assertNotEqual(li_sqr_out[0], s1)

if __name__ == '__main__':
    unittest.main()
