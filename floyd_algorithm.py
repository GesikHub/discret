import numpy as np


def floyd(adjacency_list, points):
    way_matrix = create_matrix(adjacency_list, points)
    for i in range(int(way_matrix.size ** 0.5)):
        for j in range(int(way_matrix.size ** 0.5)):
            if (not(i == j)) and (way_matrix[i][j] == 0):
                way_matrix[i][j] = 100

    for k in range(int(way_matrix.size ** 0.5)):
        for i in range(int(way_matrix.size ** 0.5)):
            for j in range(int(way_matrix.size ** 0.5)):
                if way_matrix[i][k] + way_matrix[k][j] < way_matrix[i][j]:
                    way_matrix[i][j] = way_matrix[i][k] + way_matrix[k][j]


def create_matrix(adjacency_list, points):
    adjacency_matrix = np.zeros((points.__len__(), points.__len__()))
    for i in range(1, points.__len__() + 1):
        for edge in adjacency_list[i]:
            adjacency_matrix[i - 1][edge.arrivalPointId - 1] = edge.price
    return adjacency_matrix
