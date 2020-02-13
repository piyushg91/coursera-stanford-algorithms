import time
import heapq
from piyush_utils.basic_funcs import BasicFuncs
from typing import Dict


class Assignment2(object):
    def __init__(self, input_graph: Dict[str, Dict[str, int]]):
        self.graph = input_graph
        self.num_of_nodes = len(input_graph.keys())

    def apply_djikastra_algorithm(self, starting_node: str):
        seen = set()
        dist_dict = {}
        frontier = [(0, starting_node, starting_node)]

        while len(seen) < self.num_of_nodes:
            # Pick the node with the smallest distance
            cost, start, end = heapq.heappop(frontier)
            if end in seen:
                continue
            seen.add(end)
            # print('{0} {1}\n'.format(end, cost))
            dist_dict[end] = cost
            for outgoing_node in self.graph[end]:
                if outgoing_node not in seen:
                    new_cost = cost + self.graph[end][outgoing_node]
                    tup = (new_cost, end, outgoing_node)
                    heapq.heappush(frontier, tup)
            # Sort the frontier based on cost
        return dist_dict


if __name__ == '__main__':
    s = BasicFuncs.load_file_as_string('task-2.txt')
    graph = {}
    for line in s.splitlines():
        line = line.rstrip()
        raw_list = line.split('\t')
        node = raw_list[0]
        if node not in graph:
            graph[node] = {}
        for edge in raw_list[1:]:
            outgoing_node, weight = edge.split(',')
            graph[node][outgoing_node] = int(weight)
            if outgoing_node not in graph:
                graph[outgoing_node] = {}
    solver = Assignment2(graph)
    output = solver.apply_djikastra_algorithm('1')
    s = '7,37,59,82,99,115,133,165,188,197'
    answers = [str(output[d]) for d in s.split(',')]
    answers = ','.join(answers)
    print(answers)
