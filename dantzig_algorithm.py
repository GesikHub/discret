import numpy as np


def dantzig_algorithm(adjacency_list, points):
    way_matrix = create_matrix(adjacency_list, points)
    adjacency_matrix = way_matrix
    for i in range(int(way_matrix.size ** 0.5)):
        for j in range(int(way_matrix.size ** 0.5)):
            if (not(i == j)) and (way_matrix[i][j] == 0):
                way_matrix[i][j] = 100

    for i in range(int(way_matrix.size ** 0.5)):
        minval = 100
        for j in range(int(way_matrix.size ** 0.5) - 1):
            for k in range(int(way_matrix.size ** 0.5) - 1):
                if not(i == j):
                    if(minval > way_matrix[i][j] + adjacency_matrix[j][k]):
                        minval =  way_matrix[i][j] + adjacency_matrix[j][k]
                        adjacency_matrix[i][k] = minval

            minval = 100
        for j in range(int(way_matrix.size ** 0.5) - 1):
            for k in range(int(way_matrix.size ** 0.5) - 1):
                if not(i == j):
                    if(minval > way_matrix[j][i] + adjacency_matrix[k][j]):
                        minval = way_matrix[j][i] + adjacency_matrix[k][j]
                        adjacency_matrix[k][i] = minval

        for j in range(int(way_matrix.size ** 0.5) - 1):
            for k in range(int(way_matrix.size ** 0.5) - 1):
                if not(i == j):
                    adjacency_matrix[j][k] = min(adjacency_matrix[j][i] + adjacency_matrix[i][k], adjacency_matrix[j][k])
    #print(adjacency_matrix)



def create_matrix(adjacency_list, points):
    adjacency_matrix = np.zeros((points.__len__(), points.__len__()))
    for i in range(1, points.__len__() + 1):
        for edge in adjacency_list[i]:
            adjacency_matrix[i - 1][edge.arrivalPointId - 1] = edge.price
    return adjacency_matrix