#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):


    def test_max_integet(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
