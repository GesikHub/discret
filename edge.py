class Edge:
    def __init__(self, edge):
        self.departurePointId = int(edge['DeparturePointId'])
        self.arrivalPointId = int(edge['ArrivalPointId'])
        self.price = int(edge['Price'])
    def toString(self):
        return str(self.departurePointId) + ' ' + str(self.arrivalPointId)