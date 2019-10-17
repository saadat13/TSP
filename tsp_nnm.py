import numpy as np
from utils import Point, get_point_list, dist


def print_list(lst):
    print("*" * 40)
    for p in lst:
        print(p.__str__())
    print("*" * 40)


def has_unvisited(lst):
    flag = False
    for p in lst:
        if not p.visited:
            flag = True
            break
    return flag


def generate_dist_matrix(p_list):
    n = len(p_list)
    d_matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            d = dist(p_list[i], p_list[j])
            d_matrix[i][j] = d
    return d_matrix


def nnm_calculate_shortest_path(p_list):
    dist_matrix = generate_dist_matrix(p_list)
    tmp = p_list[0]
    tmp.visited = True
    path = [tmp]
    while has_unvisited(p_list):
        min_dist = 10000
        tmp1 = None
        for p in p_list:
            d = dist_matrix[p_list.index(p)][p_list.index(tmp)]
            if not p.visited and d < min_dist:
                min_dist = d
                tmp1 = p
        tmp = tmp1
        tmp1.visited = True
        path.append(tmp1)
    path.append(p_list[0])
    return path


point_list = get_point_list()
# print path which calculated by nearest neighbor algorithm
print_list(nnm_calculate_shortest_path(point_list))
