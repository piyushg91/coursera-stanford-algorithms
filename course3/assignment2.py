from data_structures.union_find import UnionFind
from piyush_utils.basic_funcs import BasicFuncs


class Edge(object):
    def __init__(self, start: int, end: int, cost: int):
        self.start = start
        self.end = end
        self.cost = cost

class Assignment2(object):
    @staticmethod
    def clustering_1(input_file: str):
        lines = BasicFuncs.load_file_as_string(input_file).splitlines()
        num_of_nodes = int(lines[0])
        edges = []
        for line in lines[1:]:
            start, finish, cost = map(int, line.split(' '))
            edge = Edge(start, finish, cost)
            edges.append(edge)
        edges.sort(key=lambda edge: edge.cost)
        clusters = num_of_nodes
        union_find = UnionFind(num_of_nodes)
        for i, edge in enumerate(edges):
            a = edge.start - 1
            b = edge.end - 1
            if union_find.join_two_subsets(a, b):
                clusters -= 1

            if clusters <= 4:
                break
        # Compute the smallest maximum spacing
        min_max_spacing = float('inf')
        for edge in edges[i + 1:]:
            a = edge.start - 1
            b = edge.end - 1
            if not union_find.are_two_indicies_part_of_same_set(a, b):
                min_max_spacing = min(min_max_spacing, edge.cost)
        return min_max_spacing

    @staticmethod
    def clustering_2(input_file: str):
        lines = BasicFuncs.load_file_as_string(input_file).splitlines()
        nodes = int(lines[0])
        return


if __name__ == '__main__':
    # print(Assignment2.clustering_1('clustering1.txt'))
    print(Assignment2.clustering_2('clustering2.txt'))
