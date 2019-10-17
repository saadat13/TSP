import random
import time

from tsp_nnm import nnm_calculate_shortest_path
from exhaustive_search import esm_calculate_shortest_path, get_path_list
from utils import Point


def get_random_point_list(n):
    point_list = []
    for x in range(n):
        point_list.append(Point(random.randint(-20, 20), random.randint(-20, 20)))
    return point_list


p_list1 = get_random_point_list(400)
# print(p_list1)
t1 = time.clock()
nnm_calculate_shortest_path(p_list1)
print(time.clock() - t1)
p_list2 = get_random_point_list(8)
t2 = time.clock()
esm_calculate_shortest_path(get_path_list(p_list2))
print(time.clock() - t2)
