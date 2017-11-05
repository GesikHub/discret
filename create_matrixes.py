def create_adjacency_list(edges, points):
    new_edges = {point: [] for point in points}
    for i in range(1, points.__len__() + 1):
        for edge in edges:
            if edge.departurePointId == i:
                new_edges[i].append(edge)
    return new_edges


def create_adjacency_matrix(adjacency_list, points, adjacency_matrix):
    for i in range(1, points.__len__() + 1):
        for edge in adjacency_list[i]:
            adjacency_matrix[i - 1][edge.arrivalPointId - 1] = 1


def create_incidence_matrix(edges, points, incidence_matrix):
    for i in range(points.__len__()):
        for edge in edges:
            if (i + 1) ==  edge.departurePointId:
                incidence_matrix[i][edges.index(edge)] += 1
            if (i + 1) == edge.arrivalPointId:
                incidence_matrix[i][edges.index(edge)] -= 1
