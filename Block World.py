import copy
import math
import visualise

"""My visualize function recognizes the 9's that I put for the horizontal 2 element, 
which I did because there are cases where we need to know where each element is specifically, 
so if you run this without changing that you will have a grey spot"""


def set_block_orientation(quadruple):
    for i in range(4):
        for j in range(4):
            if quadruple[i][j] == 2:
                if (j < 2) and (quadruple[i][j + 1] == 2) and (quadruple[i][j + 2] != 2):  # two in a row
                    quadruple[i][j] = 9
                    quadruple[i][j + 1] = 9
                    return quadruple
                if (j == 3) and (quadruple[i][j - 1] != 2) and (quadruple[i][j + 1] == 2):  # two in a row
                    quadruple[i][j] = 9
                    quadruple[i][j + 1] = 9
                    return quadruple
                if j < 2:
                    if quadruple[i][j + 1] == 2 and quadruple[i][j + 2] == 2:  # three in a row
                        if i > 0:
                            if quadruple[i - 1][j] == 2:
                                quadruple[i][j + 1] = 9
                                quadruple[i][j + 2] = 9
                                return quadruple
                            elif quadruple[i - 1][j + 2] == 2:
                                quadruple[i][j] = 9
                                quadruple[i][j + 1] = 9
                                return quadruple
                        if i < 3:
                            if quadruple[i + 1][j] == 2:
                                quadruple[i][j + 1] = 9
                                quadruple[i][j + 2] = 9
                                return quadruple
                            elif quadruple[i + 1][j + 2] == 2:
                                quadruple[i][j] = 9
                                quadruple[i][j + 1] = 9
                                return quadruple
    return -1


def get_successors(quadruple):
    changedquadruple = copy.deepcopy(quadruple)
    resultlist = []
    for i in range(4):
        for j in range(4):
            # handling of a 2 x 2 element (notified with a 4)
            if (i < 3) and (j < 3) and (quadruple[i][j] == 4) and (quadruple[i + 1][j + 1] == 4):
                # moving downwards
                if (i < 2) and (quadruple[i + 2][j] == 0) and (quadruple[i + 2][j + 1] == 0):
                    changedquadruple[i + 2][j] = 4
                    changedquadruple[i + 2][j + 1] = 4
                    changedquadruple[i][j] = 0
                    changedquadruple[i][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving upwards
                elif (i > 1) and (quadruple[i - 1][j] == 0) and (quadruple[i - 1][j + 1] == 0):
                    changedquadruple[i - 1][j] = 4
                    changedquadruple[i - 1][j + 1] = 4
                    changedquadruple[i + 1][j] = 0
                    changedquadruple[i + 1][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                    # else skip this case because it has a higher cost
                # moving right
                elif (j < 2) and (quadruple[i][j + 2] == 0) and (quadruple[i + 1][j + 2] == 0):
                    changedquadruple[i][j + 2] = 4
                    changedquadruple[i + 1][j + 2] = 4
                    changedquadruple[i][j] = 0
                    changedquadruple[i + 1][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                    # else skip this case because it has a higher cost
                # moving left
                elif (j > 0) and (quadruple[i][j - 1] == 0) and (quadruple[i + 1][j - 1] == 0):
                    changedquadruple[i][j - 1] = 4
                    changedquadruple[i + 1][j - 1] = 4
                    changedquadruple[i][j + 1] = 0
                    changedquadruple[i + 1][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)

            # handling of a horizontal 2 x 1 element (notified with a 9) !! multiple results possible
            if (j < 3) and (quadruple[i][j] == 9) and (quadruple[i][j + 1] == 9):
                # moving right
                if (j < 2) and (quadruple[i][j + 2] == 0):
                    changedquadruple[i][j + 2] = 9
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving left
                if (j > 0) and (quadruple[i][j - 1] == 0):
                    changedquadruple[i][j - 1] = 9
                    changedquadruple[i][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # else skip this case because it has a higher cost
                # moving downwards
                elif (i < 3) and (quadruple[i + 1][j] == 0) and (quadruple[i + 1][j + 1] == 0):
                    changedquadruple[i + 1][j] = 9
                    changedquadruple[i + 1][j + 1] = 9
                    changedquadruple[i][j] = 0
                    changedquadruple[i][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving upwards
                elif (i > 0) and (quadruple[i - 1][j] == 0) and (quadruple[i - 1][j + 1] == 0):
                    changedquadruple[i - 1][j] = 9
                    changedquadruple[i - 1][j + 1] = 9
                    changedquadruple[i][j] = 0
                    changedquadruple[i][j + 1] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)

            # handling of a vertical 2 x 1 element (notified with a 2) !! multiple results possible
            if (i < 3) and (quadruple[i][j] == 2) and (quadruple[i + 1][j] == 2):
                # moving downwards
                if (i < 2) and (quadruple[i + 2][j] == 0):
                    changedquadruple[i + 2][j] = 2
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving upwards
                if (i > 0) and (quadruple[i - 1][j] == 0):
                    changedquadruple[i - 1][j] = 2
                    changedquadruple[i + 1][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving right
                elif (j < 3) and (quadruple[i][j + 1] == 0) and (quadruple[i + 1][j + 1] == 0):
                    changedquadruple[i][j + 1] = 2
                    changedquadruple[i + 1][j + 1] = 2
                    changedquadruple[i][j] = 0
                    changedquadruple[i + 1][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving left
                elif (j > 0) and (quadruple[i][j - 1] == 0) and (quadruple[i + 1][j - 1] == 0):
                    changedquadruple[i][j - 1] = 2
                    changedquadruple[i + 1][j - 1] = 2
                    changedquadruple[i][j] = 0
                    changedquadruple[i + 1][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                    # else skip this case because it has a higher cost
            # handling of a 1 x 1 element (notified with a 1) !! multiple results possible
            if quadruple[i][j] == 1:
                # moving downwards
                if (i < 3) and (quadruple[i + 1][j] == 0):
                    changedquadruple[i + 1][j] = 1
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving upwards
                if (i > 0) and (quadruple[i - 1][j] == 0):
                    changedquadruple[i - 1][j] = 1
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving right
                if (j < 3) and (quadruple[i][j + 1] == 0):
                    changedquadruple[i][j + 1] = 1
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
                # moving left
                if (j > 0) and (quadruple[i][j - 1] == 0):
                    changedquadruple[i][j - 1] = 1
                    changedquadruple[i][j] = 0
                    resultlist.append(changedquadruple)
                    changedquadruple = copy.deepcopy(quadruple)
    return resultlist


class Node():
    def __init__(self, quadruple, parent, cost):
        self.parent = parent
        self.quadruple = quadruple
        self.cost = cost


def a_star_heuristic(quadruple):
    for i in range(4):
        for j in range(4):
            if quadruple[i][j] == 4:
                return math.sqrt((3 - (i + 1)) ** 2 + j ** 2)


def search(quadruple, type):
    visited = set()
    pq, goal = [], None
    quadruple = set_block_orientation(quadruple)
    if type == "a*s":
        cost = a_star_heuristic(quadruple) + 1
    else:
        cost = 1
    init_node = Node(quadruple, 0, cost)
    pq.append(init_node)
    while True:
        if pq[0].quadruple[3][0] == 4:
            goal = pq[0]
            break
        for child in get_successors(pq[0].quadruple):
            if tuple(tuple(s) for s in child) in visited:
                continue
            visited.add(tuple(tuple(s) for s in child))
            if type == "a*s":
                cost = a_star_heuristic(child) + 1
            else:
                cost = 1
            node = Node(child, pq[0], cost)
            pq.append(node)
        pq.pop(0)
        pq.sort(key=lambda node: node.cost)
    return generate_successful_path(goal)


def generate_successful_path(node):
    path = []
    while node.parent != 0:
        path.append(node.quadruple)
        node = node.parent
    path.append(node.quadruple)
    path.reverse()
    return path


def uniform_cost_search(quadruple):
    return search(quadruple, "ucs")


def a_star_search(quadruple):
    return search(quadruple, "a*s")


# ------- testsets--------
initialquadruple = [[1, 2, 1, 1], [1, 2, 4, 4], [2, 2, 4, 4], [1, 1, 0, 0]]
# initialquadruple = [[4, 4, 1, 1], [4, 4, 2, 1], [1, 1, 2, 1], [2, 2, 0, 0]]
# initialquadruple = [[1, 2, 2, 2], [1, 4, 4, 2], [1, 4, 4, 1], [1, 0, 0, 1]]


print("\nprogramm runs with uniform cost search")
path = uniform_cost_search(initialquadruple)

# print("\nprogramm runs with a* search")
# path = a_star_search(initialquadruple)

visualise.start_simulation(path)


