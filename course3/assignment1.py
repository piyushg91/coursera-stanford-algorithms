from queue import PriorityQueue
from typing import List, Tuple
from piyush_utils.basic_funcs import BasicFuncs
from data_structures.union_find import UnionFind


class Edge(object):
    def __init__(self, start: int, end: int, cost: int):
        self.start = start
        self.end = end
        self.cost = cost


class Assignment1(object):
    @classmethod
    def scheduling_app(cls, file_name: str):
        s = BasicFuncs.load_file_as_string(file_name)
        jobs = []
        for line in s.splitlines()[1:]:
            weight, length = line.split(' ')
            weight, length = int(weight), int(length)
            difference = weight - length
            ratio = weight/length
            job_info = (weight, length, difference, ratio)
            jobs.append(job_info)

        # Part 1 problem
        jobs.sort(key=lambda x: (x[2], x[0]))
        jobs.reverse()
        decreasing_times = cls.get_weighted_sums(jobs)

        # Part 2 problem
        jobs.sort(key=lambda x: x[3])
        jobs.reverse()
        ratio_times = cls.get_weighted_sums(jobs)
        return [decreasing_times, ratio_times]


    @classmethod
    def get_weighted_sums(cls, jobs: List[Tuple]):
        total_weighted_completion_time = 0
        time_so_far = 0
        for job in jobs:
            weight, length, _, _ = job
            time_so_far += length
            job_weight = weight * time_so_far
            total_weighted_completion_time += job_weight
        return total_weighted_completion_time

    @staticmethod
    def prims_algorithm(edges_file: str):
        s = BasicFuncs.load_file_as_string(edges_file)
        lines = s.splitlines()
        first_line = lines[0]
        num_of_nodes, num_of_edges = map(int, first_line.split(' '))
        graph = {}
        for line in lines[1:]:
            start, finish, cost = map(int, line.split(' '))
            if start not in graph:
                graph[start] = {finish: cost}
            else:
                if finish in graph[start]:
                    graph[start][finish] = min(graph[start][finish], cost)
                else:
                    graph[start][finish] = cost
            if finish not in graph:
                graph[finish] = {start: cost}
            else:
                if start in graph[finish]:
                    graph[finish][start] = min(graph[finish][start], cost)
                else:
                    graph[finish][start] = cost

        # Prims algorithm
        seen = set()
        pq = PriorityQueue()

        pq.put((0, 1))

        mst_sum = 0
        while len(seen) < num_of_nodes:
            node_cost, node = pq.get()
            if node in seen:
                continue
            seen.add(node)
            connections = graph[node]
            mst_sum += node_cost
            for connection in connections.keys():
                if connection not in seen:
                    relative_cost = connections[connection]
                    info = (relative_cost, connection)
                    pq.put(info)
        return mst_sum

    @staticmethod
    def kruskals_algorithm(edges_file: str):
        s = BasicFuncs.load_file_as_string(edges_file)
        lines = s.splitlines()
        first_line = lines[0]
        num_of_nodes, num_of_edges = map(int, first_line.split(' '))
        union_find = UnionFind(num_of_nodes)
        edges = []
        for line in lines[1:]:
            start, end, cost = map(int, line.split(' '))
            edge = Edge(start, end, cost)
            edges.append(edge)
        edges.sort(key=lambda x: x.cost)
        min_span_tree_cost = 0
        for edge in edges:
            a = edge.start - 1
            b = edge.end - 1
            if union_find.join_two_subsets(a, b):
                min_span_tree_cost += edge.cost

        return min_span_tree_cost




if __name__ == '__main__':
    # print(Assignment1.scheduling_app('jobs.txt'))
    print(Assignment1.kruskals_algorithm('edges.txt'))
