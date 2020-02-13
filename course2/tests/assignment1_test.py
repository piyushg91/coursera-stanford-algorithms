from piyush_utils.base_test_case import BaseTestCase
from coursera.course2.assignment1 import Assignment1



class Assignment1Test(BaseTestCase):
    def setUp(self):
        graph = {
            1: {5},
            2: {3},
            3: {4},
            4: {2, 5},
            5: {6},
            6: {1, 9},
            7: {8},
            8: {9},
            9: {7}
        }
        self.task = Assignment1(graph)

    def test_reverse_edges(self):
        valid_reversed = {
            1: {6},
            2: {4},
            3: {2},
            4: {3},
            5: {1, 4},
            6: {5},
            7: {9},
            8: {7},
            9: {6, 8}
        }
        reversed_graph = self.task.reverse_edges()
        self.assertEqual(reversed_graph, valid_reversed)

    def test_reverse_edges2(self):
        task = Assignment1({1: {2, 3}})
        valid_reversed = {
            2: {1},
            3: {1},
            1: set()
        }
        self.assertEqual(valid_reversed, task.reverse_edges())

    def test_finishing_order(self):
        correct_order = [7, 8, 1, 2, 3, 4, 5, 6, 10]
        reversed_graph = self.task.reverse_edges()
        self.task.run_dfs_pass1(reversed_graph)
        self.assertEqual(correct_order, self.task.finishing_order)

    def test_bleh(self):
        self.task.solve_problem()