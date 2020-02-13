from typing import List
from piyush_utils.basic_funcs import BasicFuncs


class Assignment4(object):
    def __init__(self, raw_data: List[int], lower_sum_bound: int, upper_sum_bound: int):
        self.sorted = sorted(raw_data)
        self.lower_sum = lower_sum_bound
        self.higher_sum = upper_sum_bound

    def binary_search_for_indicies(self, x) -> List[int]:
        lower_y = self.lower_sum - x
        upper_y = self.higher_sum - x
        i1 = self.binary_search_for_lower_bound(lower_y, 'lower')
        i2 = self.binary_search_for_lower_bound(upper_y, 'upper')
        if i1 == -1 or i2 == -1:
            return []
        return list(range(i1, i2 + 1))

    def binary_search_for_lower_bound(self, target_bound, bound):
        # Base cases
        mid_point = -1
        if bound == 'lower':
            if self.sorted[-1] < target_bound:
                return mid_point
        else:
            if self.sorted[0] > target_bound:
                return mid_point
        first = 0
        last = self.sorted.__len__() -1
        max_index = self.sorted.__len__() - 1
        while first < last:
            mid_point = int((last + first)/2)
            if self.sorted[mid_point] == target_bound:
                if bound == 'lower':
                    while mid_point > 0 and self.sorted[mid_point - 1] == target_bound:
                        mid_point -= 1
                else:
                    while mid_point < max_index and self.sorted[mid_point + 1] == target_bound:
                        mid_point += 1
                return mid_point
            else:
                if self.sorted[mid_point] > target_bound:
                    last = mid_point - 1
                else:
                    first = mid_point + 1
        if bound == 'lower' and self.sorted[last] < target_bound:
            return last + 1
        if bound == 'upper' and self.sorted[last] > target_bound:
            return last - 1
        return last

    def get_indicies(self):
        # index_count_map = {}
        seen_pairs = set()
        seen_totals = set()
        for i, x in enumerate(self.sorted):
            indicies = self.binary_search_for_indicies(x)
            for j in indicies:
                y = self.sorted[j]
                total = x + y
                if x == y or (x, y) in seen_pairs or (y, x) in seen_pairs or total in seen_totals:
                    continue
                seen_pairs.add((x, y))
                seen_totals.add(total)
                # if j in index_count_map:
                #     index_count_map[j] += 1
                # else:
                #     index_count_map[j] = 1
        # count = 0
        # for key in index_count_map:
        #     if index_count_map[key] == 1:
        #         count += 1
        sum_set = set()
        for pair in seen_pairs:
            total = pair[0] + pair[1]
            if total in sum_set:
                print(total)
            sum_set.add(total)
        return seen_pairs.__len__()

    @staticmethod
    def load_file_as_array(file_path: str):
        s = BasicFuncs.load_file_as_string(file_path)
        array = []
        for i in s.splitlines():
            array.append(int(i))
        return array


if __name__ == '__main__':
    array = Assignment4.load_file_as_array('task-4.txt')
    # array = [-2, 0, 0, 4]
    solver = Assignment4(array, -10000, 10000)
    print(solver.get_indicies())
    print('yollo')
    # count = 0
    # for i, first in enumerate(array):
    #     for j, second in enumerate(array[i + 1:]):
    #         total = first + second
    #         if total <= 10000 and total >= -10000:
    #             count += 1
    # print(count)
