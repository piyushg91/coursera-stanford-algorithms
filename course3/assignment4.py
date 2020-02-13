import time
from piyush_utils.basic_funcs import BasicFuncs


class Assignment4(object):
    @staticmethod
    def problem1(input_file: str):
        lines = BasicFuncs.load_file_as_string(input_file).splitlines()
        catalog = []
        for i in lines[1:]:
            value, cost = i.split(' ')
            catalog.append((int(value), int(cost)))
        max_weight, num_of_items = lines[0].split(' ')
        max_weight, num_of_items = int(max_weight), int(num_of_items)

        matrix = []
        first_vector = []
        first_weight, first_value = catalog[0][1], catalog[0][0]
        for weight_allowed in range(max_weight + 1):
            if weight_allowed >= first_weight:
                first_vector.append(first_value)
            else:
                first_vector.append(0)
        matrix.append(first_vector)
        optimal_value = 0
        for item_index in range(1, num_of_items):
            item = catalog[item_index]
            current_weight, current_value = item[1], item[0]
            item_vector = []
            for weight_allowed in range(max_weight + 1):
                case1_excluded = matrix[item_index - 1][weight_allowed]
                if weight_allowed < current_weight:
                    item_vector.append(case1_excluded)
                    continue
                case2_included = matrix[item_index -1][weight_allowed - current_weight] + current_value
                item_vector.append(max(case1_excluded, case2_included))
            matrix.append(item_vector)
            optimal_value = max(optimal_value, max(item_vector))

        return item_vector[-1]

    @staticmethod
    def problem2(input_file: str):
        lines = BasicFuncs.load_file_as_string(input_file).splitlines()
        catalog = []
        for i in lines[1:]:
            value, cost = i.split(' ')
            catalog.append((int(value), int(cost)))
        max_weight, num_of_items = lines[0].split(' ')
        max_weight, num_of_items = int(max_weight), int(num_of_items)

        first_vector = []
        first_weight, first_value = catalog[0][1], catalog[0][0]
        for weight_allowed in range(max_weight + 1):
            if weight_allowed >= first_weight:
                first_vector.append(first_value)
            else:
                first_vector.append(0)
        last_vector = first_vector
        for item_index in range(1, num_of_items):
            item = catalog[item_index]
            current_weight, current_value = item[1], item[0]
            item_vector = last_vector.copy()
            for weight_allowed in range(current_weight, max_weight + 1):
                case1_excluded = last_vector[weight_allowed]
                case2_included = last_vector[weight_allowed - current_weight] + current_value
                item_vector[weight_allowed] = max(case1_excluded, case2_included)
            last_vector = item_vector
            if item_index % 200 == 0:
                print(item_index)

        return last_vector[-1]


if __name__ == '__main__':
    a = time.time()
    print(Assignment4.problem1('knapsack.txt'))
    # print(Assignment4.problem2('knapsack_big.txt'))
    b = time.time()
    print(b-a)
