def search_way(adjacency_list, points):
    use = [False for i in range(points.__len__())]
    way = [0 for i in range(points.__len__())]
    cost = [100000 for i in range(points.__len__())]
    cost[0] = 0
    checkVar = 0
    test = True
    while test:
        min = 100000
        for i in range(points.__len__()):
            if (cost[i] < min) and (not use[i]):
                checkVar = i
                min = cost[i]
        for i in range(adjacency_list[checkVar + 1].__len__()):
                bestStation = adjacency_list[checkVar + 1][i].arrivalPointId - 1
                bestValue = adjacency_list[checkVar + 1][i].price
                if(cost[i] +  bestValue < cost[bestStation]):
                    way[bestStation] = adjacency_list[checkVar + 1][i]
                    cost[bestStation] = cost[checkVar] + bestValue
        use[checkVar] = True
        test = False
        for i in range(adjacency_list[checkVar + 1].__len__()):
            if use[i] == False:
                test = True
    print(cost)
    print(points)
    return way;