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

    def test_non_list(self):
        """This module checks for non lists
        """
        self.assertTrue(max_integer([]))  # Test an empty list
        self.assertTrue(max_integer([1, 2, 3]))  # Test a non-empty list
        self.assertFalse(max_integer("not a list"))  # Test a string
        self.assertFalse(max_integer(42))  # Test an int
        self.assertFalse(max_integer({"key": "value"}))  # Test a dictionary


if __name__ == '__main__':
    main()
