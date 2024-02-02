#!/usr/bin/python3
"""5. Max integer - Unittest"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that defines tests for maximum integer in list"""

    def test_unsigned(self):
        """Function to test for unsigned integers in normal list"""

        self.assertEqual(max_integer([13, -4, 105, 9]), 105)

    def test_empty(self):
        """Function to test an empty list"""

        self.assertEqual(max_integer([]), None)

    def test_repeated(self):
        """Function to test repeated integers"""

        self.assertEqual(max_integer([47, 2023, 2023]), 2023)

    def test_float(self):
        """Function to test floating point values"""

        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)

    def test_operators(self):
        """Function to test lists with operations in them"""

        self.assertEqual(max_integer([-3, -6 * -6, 12, -1]), 36)

    def test_negative(self):
        """Function to test negative numbers in list"""

        self.assertEqual(max_integer([-13, -45, -21, -1]), -1)

    def test_max_first(self):
        """Function to test list with max num in front"""

        self.assertEqual(max_integer([2023, 18, 1, 5, 9]), 2023)

    def test_zeros(self):
        """Function to test list with zros"""

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_huge(self):
        """Function to test a very big list"""

        self.assertEqual(max_integer([
            1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
            2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
            2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027,
            2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037,
            2038, 2039, 2040, 2041]), 2041)

    def test_iteration(self):
        """Function to test with iteration through list"""

        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 6 for i in my_list]), 30)

    def test_single_elem(self):
        """Function to test list with only one element"""

        self.assertEqual(max_integer([13]), 13)

    def test_string(self):
        """Function to test list with strings"""

        with self.assertRaises(TypeError):
            max_integer([0, '13'])

    def test_tuple(self):
        """Function to test list with tuple element"""

        with self.assertRaises(TypeError):
            max_integer([116, (13, 4777)])

    def test_dictionary(self):
        """Function to test list with dictionary element"""

        with self.assertRaises(KeyError):
            max_integer({'first': 100, 'second': 200})

    def test_number(self):
        """Function to test single integer not in list"""

        with self.assertRaises(TypeError):
            max_integer(1)

