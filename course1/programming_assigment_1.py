from unittest import TestCase
from probability.binomials import Probability
from piyush_utils.basic_funcs import BasicFuncs
from data_structures.sorting import MergeSort, QuickSort


class Solution(object):
    @classmethod
    def karatsuba(cls, inp1: int, inp2: int):
        """ Making a few assumptions. 1) size of inps is 2**some number and both are the same size
        :param inp1:
        :param inp2:
        :return:
        """
        s1, s2 = str(inp1), str(inp2)
        len1, len2 = len(s1), len(s2)
        mid1 = int(len1/2)
        mid2 = int(len2/2)
        a, b = s1[:mid1], s1[mid1:]
        c, d = s2[:mid2], s2[mid2:]
        if len(a) <= 2:
            ac = int(a) * int(c)
            bd = int(b) * int(d)
        else:
            ac = cls.karatsuba(int(a), int(c))
            bd = cls.karatsuba(int(b), int(d))
        ad_plus_bc = (int(a) + int(b))*(int(c) + int(d)) - ac - bd
        x_y = (10**len1) * ac + ad_plus_bc*(10**(len1/2)) + bd # TODO
        return x_y

    @classmethod
    def week2(cls):
        s = BasicFuncs.load_file_as_string('inversion.txt')
        array = []
        for line in s.splitlines():
            array.append(int(line))
        m = MergeSort(array)
        print(m.count_inversions())

    @classmethod
    def week3(cls):
        s = BasicFuncs.load_file_as_string('quick-sort.txt')
        array = []
        for line in s.splitlines():
            line = line.rstrip().lstrip()
            array.append(int(line))
        sorter = QuickSort(array)
        sorter.sort('med')
        print(sorter.comparisons)


class SolutionTest(TestCase):
    def test1(self):
        output = Solution.karatsuba(5678, 1234)
        self.assertEqual(output, 7006652)

    def test2(self):
        a = 3141592653589793238462643383279502884197169399375105820974944592
        b = 2718281828459045235360287471352662497757247093699959574966967627
        valid = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
        output = Solution.karatsuba(a, b)
        self.assertEqual(output, valid)

    def test3(self):
        Solution.week3()
        # part1 : 162085
        # part2: 164123
        # part3: 138382
