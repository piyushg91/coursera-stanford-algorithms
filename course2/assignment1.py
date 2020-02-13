import heapq
from typing import Dict, Set
from piyush_utils.basic_funcs import BasicFuncs


class Assignment1(object):
    def __init__(self, input_graph: Dict[int, Set[int]]):
        self.input_graph = input_graph
        self.t = 0  # Global variable to keep track of how many nodes, needs to manually resetted
        self.finishing_order = []

    def reset_global_variables(self):
        self.t = 0
        self.finishing_order = []

    def reverse_edges(self):
        new_graph = {}
        for node in self.input_graph.keys():
            if node not in new_graph:
                new_graph[node] = set()
            for connection in self.input_graph[node]:
                if connection in new_graph:
                    new_graph[connection].add(node)
                else:
                    new_graph[connection] = {node}
        return new_graph

    def run_dfs_pass1(self, input_graph):
        explored = set()
        keys = reversed(sorted(input_graph.keys()))
        for i in keys:
            if i not in explored:
                self.run_dfs_with_times(input_graph, i, explored)

    def run_dfs_pass2(self):
        """ Assumes you've ran pass 1
        :return:
        """
        order = reversed(self.finishing_order)
        self.reset_global_variables()
        explored = set()
        max_heap = []
        for i in order:
            if i not in explored:
                self.run_dfs_with_times(self.input_graph, i, explored)
                l = self.finishing_order.__len__()
                heapq.heappush(max_heap, -1*l)
                self.reset_global_variables()
        answers = []
        for _ in range(5):
            answers.append(str(-1 * heapq.heappop(max_heap)))
        print(','.join(answers))

    def run_dfs_with_times(self, input_graph, starting_node: int, explored: Set[int]):
        stack = [starting_node]

        while stack:
            current = stack[-1]
            explored.add(current)
            for conn in input_graph[current]:
                if conn in explored:
                    continue
                stack.append(conn)
                break
            else:
                last = stack.pop()
                self.finishing_order.append(last)

    def solve_problem(self):
        reversed_edges = self.reverse_edges()
        self.run_dfs_pass1(reversed_edges)
        self.run_dfs_pass2()


if __name__ == '__main__':

    graph = {}
    s = BasicFuncs.load_file_as_string('task-1.txt')
    for line in s.splitlines():
        line = line.rstrip()
        node, connect = line.split(' ')
        node = int(node)
        connect = int(connect)
        if node in graph:
            graph[node].add(connect)
        else:
            graph[node] = {connect}
        if connect not in graph:
            graph[connect] = set()

    print('Done loading from file')
    a = Assignment1(graph)
    a.solve_problem()

