from itertools import permutations

from utils import Point, get_point_list, dist


def get_points_permutations(lst, perm):
    perm_list = []
    for i in perm:
        perm_list.append(lst[i])
    return perm_list


def get_path_list(point_list):
    n = len(point_list)
    perms = list(permutations(range(1, n)))
    path_list = []
    for p in perms:
        perm_list = [point_list[0]]
        perm_list.extend(get_points_permutations(point_list, p))
        perm_list.extend([point_list[0]])
        path_list.append(perm_list)

    for path in path_list:
        length = 0
        p1 = path[0]
        for p in path:
            length += dist(p1, p)
            p1 = p
        path.append({"length": length})
    return path_list


def esm_calculate_shortest_path(path_list):
    min_dist = float(path_list[0][len(path_list[0]) - 1]['length'])
    final_path = path_list[0]
    for path in path_list:
        l = path[len(path)-1]['length']
        if l < min_dist:
            min_dist = l
            final_path = path
    return final_path


point_list = get_point_list()
path_list = get_path_list(point_list)
print("path list : \n", path_list)
print("shortest path: \n", esm_calculate_shortest_path(path_list))
