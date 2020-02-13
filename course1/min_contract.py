import random
import re
from copy import  deepcopy
from typing import Dict, List
from unittest import TestCase
from piyush_utils.basic_funcs import BasicFuncs


class MinContract(object):
    def __init__(self, graph: Dict[int, List[int]], edge_count: int):
        self.graph = graph
        self.edge_count = edge_count
        self.original = deepcopy(graph)

    def reset_to_original(self):
        self.graph = deepcopy(self.original)

    def collapse_edge(self, start_node: int, end_node: int):
        for edge in self.graph[end_node]:
            if edge == start_node:
                continue
            self.graph[start_node].append(edge)
            self.graph[edge].remove(end_node)
            self.graph[edge].append(start_node)
            self.graph[edge].sort()
        del self.graph[end_node]
        while end_node in self.graph[start_node]:
            self.graph[start_node].remove(end_node)

    def randomly_contract(self):
        while len(self.graph) > 2:
            verticies = self.graph.keys()
            selected_start = random.sample(verticies, 1)[0]
            selected_end = random.sample(self.graph[selected_start], 1)[0]
            self.collapse_edge(selected_start, selected_end)
        first, second = self.graph.keys()
        assert len(self.graph[first]) == len(self.graph[second])
        return len(self.graph[first])


    @staticmethod
    def load_graph_from_file(file_path: str):
        s = BasicFuncs.load_file_as_string(file_path)
        adj_set_list = {}
        num_of_edges = 0
        for line in s.splitlines():
            nums = re.split('\t|\s', line)
            node = int(nums[0])
            adj_set_list[node] = []
            for i in nums[1:]:
                if i == '':
                    continue
                vertex_conn = int(i)
                adj_set_list[node].append(vertex_conn)
                num_of_edges += 1
        num_of_edges = num_of_edges/2
        return adj_set_list, num_of_edges

    @staticmethod
    def solve_assignment(file_path):
        min_edges = 25
        g, edges = MinContract.load_graph_from_file(file_path)
        count = len(g)
        print('Running {0} iterations'.format(count*count))
        contractor = MinContract(g, edges)
        for i in range(count*count):
            if i % 100 == 0:
                print('Running iteration number ' + str(i))
            edges = contractor.randomly_contract()
            if edges < min_edges:
                min_edges = edges
                print('Ran {0} iterations so far and got {1} min edges'.format(i, min_edges))
            contractor.reset_to_original()
        return min_edges


if __name__ == '__main__':
    MinContract.solve_assignment('min-cut.txt')
