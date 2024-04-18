from collections import defaultdict
import sys


class Graph:
    def __init__(self, size):
        self.edges = defaultdict(list)  # dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}  # dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size  # number of graph's node
        self.dist = []  # list to store distance from start node
        for i in range(size):
            self.dist.append(sys.maxsize)  # maximum initial value
        self.previous = []  # list to store previous node
        for i in range(size):
            self.previous.append(None)  # initial value None

    # connect node A and node B in both directions and set the weight to weight
    def add_edge(self, from_node, to_node, weight):  # bidirectional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    # find and return the node with the smallest distance from Q
    def findSmallestNode(self):
        smallest = self.dist[self.getIndex(self.Q[0])]
        result = self.getIndex(self.Q[0])
        for i in range(len(self.dist)):
            if self.dist[i] < smallest:
                node = self.unpoppedQ[i]
                if node in self.Q:
                    smallest = self.dist[i]
                    result = self.getIndex(node)
        return result

    # return the index of neighbour
    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):
            if neighbour == self.unpoppedQ[i]:
                return i

    # return index of uNode
    def getPopPosition(self, uNode):
        result = 0
        for i in range(len(self.Q)):
            if self.Q[i] == uNode:
                return i
        return result

    # return unvisited nodes associated with uNode as a list
    def getUnvisitedNodes(self, uNode):
        resultList = []
        allNeighbours = self.edges[uNode]
        for neighbour in allNeighbours:
            if neighbour in self.Q:
                resultList.append(neighbour)
        return resultList

    def dijsktra(self, start, end):
        self.Q = []
        for key in self.edges:
            self.Q.append(key)  # Q = list of non visited nodes
        for i in range(len(self.Q)):
            if self.Q[i] == start:
                self.dist[i] = 0
        self.unpoppedQ = self.Q[0:]

        while self.Q:
            u = self.findSmallestNode()  # find the vertex with the smallest distance
            if self.dist[u] == sys.maxsize:  # there is no route to destination so break
                break
            if self.unpoppedQ[u] == end:  # we’ve reached the destination
                break

            uNode = self.unpoppedQ[u]

            self.Q.pop(self.getPopPosition(uNode))  # remove the smallest node, u from graph, Q
            neighbour = self.getUnvisitedNodes(uNode) # get all the unvisited neighbour nodes
            for v in neighbour:  # find the connected neighbours node
                vIndex = self.getIndex(v)
                alt = self.dist[u] + self.weights[tuple(uNode + v)] # calculated the distance between nodes
                if alt < self.dist[vIndex]:  # if the new distance is smaller than the previous distance
                    self.dist[vIndex] = alt  # update distance and previous node
                    self.previous[vIndex] = uNode

        shortest_path = []
        shortest_path.insert(0, end)
        u = self.getIndex(end)
        while self.previous[u] is not None:
            shortest_path.insert(0, self.previous[u])
            u = self.getIndex(self.previous[u])
        return shortest_path, self.dist[self.getIndex(end)]


graph = Graph(8)

edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]

for edge in edges:
    graph.add_edge(*edge)

print(graph.dijsktra('O', 'T'))
