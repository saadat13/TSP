from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return str(self)


def dist(p1, p2):
    return sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2))


def get_point_list():
    point_list = []
    n = int(input())
    for i in range(n):
        str_in = str(input()).split(' ')
        x, y = int(str_in[0]), int(str_in[1])
        point_list.append(Point(x, y))
    return point_list
