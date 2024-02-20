import math


def distanceParse(matrix, points, dimensions):
    for x in range(len(matrix)-1):
        for y in range(x + 1, len(matrix)):
            matrix[x][y] = multidimensional_distance(points[x], points[y], dimensions)
    for x in range(len(matrix)):
        matrix[x][x] = 2.0
    for x in range(len(matrix)-1):
        for y in range(x + 1, len(matrix)):
            matrix[y][x] = matrix[x][y]
    return matrix


def multidimensional_distance(node1, node2, dimensions):
    if len(node1) != len(node2) or len(node1) != dimensions:
        raise ValueError("Nodes have different dimensions than the graph.")

    sum_of_squares = sum((node1[i] - node2[i]) ** 2 for i in range(dimensions))
    return max(0.0, 2 - math.sqrt(sum_of_squares))


def digest(intelligence):
    dimensions = intelligence.dimensions
    cnt = len(intelligence.nodes)
    matrix = [[0.0] * cnt for _ in range(cnt)]

    matrix = distanceParse(matrix, [node.location for node in intelligence.nodes], dimensions)
    return matrix
