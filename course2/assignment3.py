import heapq
from piyush_utils.basic_funcs import BasicFuncs


class ProgrammingAssignment1(object):
    def __init__(self):
        self.min_heap = [] # Represents the right half of the array
        self.max_heap = [] # Represents the left half of the array
        self.elements_added = 0

    def balance_trees(self):
        diff_in_len = self.min_heap.__len__() - self.max_heap.__len__()
        if diff_in_len == 2:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, popped*-1)
        elif diff_in_len == -2:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, popped*-1)

    def add_new_element(self, new_element: int):
        if self.elements_added == 0:
            self.min_heap.append(new_element)
            self.elements_added += 1
            return
        # Assuming there are two elements already in there
        if new_element > self.min_heap[0]:
            heapq.heappush(self.min_heap, new_element)
        else:
            heapq.heappush(self.max_heap, new_element*-1)
        self.elements_added += 1
        self.balance_trees()

    def get_median(self):
        if self.elements_added % 2 == 0:
            return -1*self.max_heap[0]
        else:
            if self.min_heap.__len__() > self.max_heap.__len__():
                return self.min_heap[0]
            else:
                return -1 * self.max_heap[0]

    @staticmethod
    def get_med_sum(file_path: str) -> int:
        s = BasicFuncs.load_file_as_string(file_path)
        solver = ProgrammingAssignment1()
        med_sum = 0
        for line in s.splitlines():
            value = int(line)
            solver.add_new_element(value)
            median = solver.get_median()
            med_sum += median
        return med_sum % 10000


if __name__ == '__main__':
    print(ProgrammingAssignment1.get_med_sum('task-3.txt'))
    # solver = ProgrammingAssignment1()
    # a = [1, 2, 3, 4, 5, 6, 7]
    # for i in a:
    #     solver.add_new_element(i)
    # print('')