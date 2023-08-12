#!/usr/bin/python3

from unittest import TestCase, main

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(TestCase):
    """
    This class defines unittest for max_integer function
    """
    def test_empty_list(self):
        """
        This method tests if list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_ordered_unordered_lists(self):
        """
        This method checks for ordered and unordered lists
        """
        ordered_ls = [1, 2, 3, 4, 5, 6]
        unordered_ls = [5, 8, 3, 1, 4]
        self.assertEqual(max_integer(ordered_ls), 6)
        self.assertEqual(max_integer(unordered_ls), 8)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")


if __name__ == '__main__':
    main()
