from unittest import TestCase
from coursera.course1.min_contract import MinContract


class MinContractTest(TestCase):
    def setUp(self):
        graph = {
            1: [2, 3],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [2, 3]
        }
        edges = 5
        self.min_contract = MinContract(graph, edges)

    def test_collapse_edge(self):
        self.min_contract.collapse_edge(1, 2)
        valid_graph = {
            1: [3, 3, 4],
            3: [1, 1, 4],
            4: [1, 3]
        }
        self.assertEqual(valid_graph, self.min_contract.graph)
        self.min_contract.collapse_edge(1, 3)
        valid_graph = {
            1: [4, 4],
            4: [1, 1]
        }
        self.assertEqual(valid_graph, self.min_contract.graph)

    def test_collapse_edge2(self):
        self.min_contract.collapse_edge(1, 2)
        self.min_contract.collapse_edge(3, 4)
        valid_graph = {
            1: [3, 3, 3],
            3: [1, 1, 1]
        }
        self.assertEqual(valid_graph, self.min_contract.graph)
