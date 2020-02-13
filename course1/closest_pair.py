import random
from PIL import Image, ImageDraw
from typing import List, Tuple


class ClosestPair(object):
    fill_white = (255, 255, 255)

    def __init__(self, points: List[Tuple[int, int]]):
        self.points = points
        self.num_of_points = len(points)

    @staticmethod
    def get_random_points():
        x = list(range(-10, 10))
        y = list(range(-10, 10))
        random.shuffle(x)
        random.shuffle(y)
        points = []
        for i, x in enumerate(x):
            points.append((x, y[i]))
        return points

    def apply_brute_force_algorithms(self):
        closest_pairs = None
        min_dist = 10000000
        for i, p1 in enumerate(self.points):
            for j in range(i + 1, self.num_of_points):
                p2 = self.points[j]
                dist = self.get_dist_between_two_points(p1, p2)
                if dist < min_dist:
                    min_dist = dist
                    closest_pairs = (p1, p2)
        return closest_pairs

    @staticmethod
    def get_dist_between_two_points(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        term1 = x2 - x1
        term2 = y1 - y2
        return (term1**2 + term2**2)**0.5

    def visualize_points(self):
        point_size = 30
        shift = 10 * point_size
        size = (point_size*20, point_size*20)
        image = Image.new('RGB', size, color=self.fill_white)
        drawer = ImageDraw.Draw(image)
        drawer.line([0, point_size*20/2, point_size*20, point_size*20/2], fill='black', width=5)
        drawer.line([point_size*20/2, 0, point_size*20/2, point_size*20], fill='black', width=5)
        for point in self.points:
            x, y = point[0], point[1]
            y = abs(y - 10)
            x1, y1 = (x * point_size) + shift, (y * point_size)
            x2, y2 = x1 + point_size, y1 + point_size
            seq = [x1, y1, x2, y2]
            seq = [i - point_size/ 2 for i in seq]
            drawer.ellipse(seq, fill='red', outline='red')
        image.show()


if __name__ == '__main__':
    random.seed(1)
    obj = ClosestPair(ClosestPair.get_random_points())
    obj.visualize_points()
    print(obj.apply_brute_force_algorithms())


