import heapq
from binarytree import Node
from typing import Optional, List
from piyush_utils.basic_funcs import BasicFuncs


class HuffmanNode(Node):
    def __init__(self, letter: Optional[str], freq: int, max_depth: int=0, min_depth: int=0):
        self.left = None
        self.right = None
        self.letter = letter
        self.freq = freq
        self.max_depth = max_depth
        self.min_depth = min_depth
        if self.is_meta_node():
            super(HuffmanNode, self).__init__(10000 + freq)
        else:
            super(HuffmanNode, self).__init__(freq)

    def is_meta_node(self):
        return self.letter is None

    def __lt__(self, other):
        return self.freq < other.freq


class Assignment3(object):
    @staticmethod
    def apply_huffman(input_file: str) -> HuffmanNode:
        s = BasicFuncs.load_file_as_string(input_file)
        h = []
        for line in s.splitlines()[1:]:
            weight = int(line)
            node = HuffmanNode(line, weight)
            heapq.heappush(h, node)

        while h.__len__() > 1:
            first_node = heapq.heappop(h)
            sec_node = heapq.heappop(h)
            new_depth = max(first_node.max_depth, sec_node.max_depth) + 1
            new_min_depth = min(first_node.min_depth, sec_node.min_depth) + 1
            meta_node = HuffmanNode(None, first_node.freq + sec_node.freq, max_depth=new_depth, min_depth=new_min_depth)
            meta_node.left = first_node
            meta_node.right = sec_node
            heapq.heappush(h, meta_node)

        root = heapq.heappop(h)
        return root

    @classmethod
    def problem1and2(cls, input_file: str):
        root = cls.apply_huffman(input_file)
        print(root)
        return [root.max_depth, root.min_depth]

    @classmethod
    def problem3(cls, input_file: str):
        s = BasicFuncs.load_file_as_string(input_file)
        # 1, 2, 3, 4, 17, 117, 517, and 997
        verts_to_check = [0, 1, 2, 3, 16, 116, 516, 996]
        vertices = [int(line) for line in s.splitlines()[1:]]
        # vertices = [10, 30, 50, 40]
        max_weight, subset = cls.rec_get_max_weight(vertices, len(vertices) - 1)
        output = ''
        for v in verts_to_check:
            if v in subset:
                output += '1'
            else:
                output += '0'
        return output

    @classmethod
    def rec_get_max_weight(cls, vertices: List[int], final_index: int):
        mwis_array = [vertices[0]]
        if vertices[0] > vertices[1]:
            mwis_array.append(vertices[0])
        else:
            mwis_array.append(vertices[1])
        for i in range(2, vertices.__len__()):
            case1_index = i - 1
            case2_index = i - 2
            case1_max_weight = mwis_array[case1_index]
            case2_max_weight = mwis_array[case2_index]
            case2_max_weight += vertices[i]
            if case2_max_weight > case1_max_weight:
                mwis_array.append(case2_max_weight)
            else:
                mwis_array.append(case1_max_weight)
        i, to_include = final_index, []
        total = 0
        while i >= 0:
            if i == 0:
                to_include.insert(0, 0)
                break
            if i == 1:
                if mwis_array[1] > mwis_array[0]:
                    to_include.insert(0, 1)
                else:
                    to_include.insert(0, 0)
                break

            if mwis_array[i-2] + vertices[i] > mwis_array[i - 1]:
                to_include.insert(0, i)
                total += vertices[i]
                i -= 2
            else:
                i -= 1
        return total, to_include


if __name__ == '__main__':
    # print(Assignment3.problem1and2('sample-huffman.txt'))
    print(Assignment3.problem3('/home/piyush/projects/google-interview-prep/stanford-algs/testCases/course3/assignment3HuffmanAndMWIS/question3/input_random_2_10.txt'))

