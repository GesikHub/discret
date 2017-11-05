import create_matrixes as cr
import search_way as sw
import xml.etree.ElementTree as et
import dijkstras_algorithm as da
import floyd_algorithm as fl
import dantzig_algorithm as dn
import numpy as np
from edge import Edge


tree = et.ElementTree(file='test.xml')
root = tree.getroot()
edges = []
point = set()

#print(root.tag)

for child in root:
    edges.append(Edge(child.attrib))
    point.add(int(child.attrib['DeparturePointId']))
    point.add(int(child.attrib['ArrivalPointId']))

point = list(point)
point.sort()

str_matrix = '   '
for i in point:
    str_matrix += '  x' + str(i) + ' '
str_matrix += '\n'
adjacency_list = cr.create_adjacency_list(edges, point)
adjacency_matrix = np.zeros((point.__len__(), point.__len__()))
cr.create_adjacency_matrix(adjacency_list, point, adjacency_matrix)
for i in range(point.__len__()):
    if i < 9:
        str_matrix += 'x' + str(i + 1) + '  '
    else:
        str_matrix += 'x' + str(i + 1) + ' '
    for j in range(point.__len__()):
        if j < 10:
            str_matrix += ' ' + str(int(adjacency_matrix[i][j])) + '   '
        else:
            str_matrix += ' ' + str(int(adjacency_matrix[i][j])) + '     '
    str_matrix += '\n'
#print(str_matrix)
cr.create_adjacency_matrix(adjacency_list, point, adjacency_matrix)
incident_matrix = np.zeros((point.__len__(), edges.__len__()))
cr.create_incidence_matrix(edges, point, incident_matrix)
way_matrix = np.zeros((point.__len__(), point.__len__()))
way_matrix = sw.search_way(adjacency_matrix)
way = da.search_way(adjacency_list, point)
fl.floyd(adjacency_list, point)
dn.dantzig_algorithm(adjacency_list, point)



