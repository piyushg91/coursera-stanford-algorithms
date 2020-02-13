from unittest import TestCase
from coursera.course2.assignment4 import Assignment4


class Assigment4Test(TestCase):
    def setUp(self):
        self.sample_array = [-16000, -15500, -15001, -14999, 4999, 5001, 6000, 7000, 8000]

    def test_binary_search_for_bound1(self):
        solver = Assignment4(self.sample_array)
        i = solver.binary_search_for_lower_bound(-15000, 'lower')
        self.assertEqual(i, 3)

        i = solver.binary_search_for_lower_bound(5000, 'upper')
        self.assertEqual(i, 4)

        solver = Assignment4(self.sample_array[0: 2])
        i = solver.binary_search_for_lower_bound(-15000, 'lower')
        self.assertEqual(i, -1)

        solver = Assignment4(self.sample_array[5:])
        i = solver.binary_search_for_lower_bound(5000, 'upper')
        self.assertEqual(i, -1)


