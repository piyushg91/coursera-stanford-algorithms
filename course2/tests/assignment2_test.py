from piyush_utils.base_test_case import BaseTestCase
from coursera.course2.assignment2 import Assignment2


class Assigment2Test(BaseTestCase):

    def test1(self):
        graph = {
            'A': {'B': 5, 'C': 6},
            'B': {'C': 7},
            'C': {}
        }
        valid = {
            'A': 0,
            'B': 5,
            'C': 6

        }
        solver = Assignment2(graph)
        seen = solver.apply_djikastra_algorithm('A')
        self.assertEqual(valid, seen)