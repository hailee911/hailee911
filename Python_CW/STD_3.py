class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(self.adjMatrix)
        self.size = size

                                                      # method to add a vertex to the graph
    def add_v(self, v):
        if v > self.size:                             # if the vertex is larger than the size
            new = v - self.size
            for i in range(new):                    # add an increased number of vertex into the matrix
                self.adjMatrix.append([0 for i in range(v)])
                self.size += 1

                                                      # method to add an edge to the graph
    def add_e(self, v1, v2):
        if v1 <= self.size and v2 <= self.size:       # if the vertices are not over limit
            if not self.adjMatrix[v1 - 1][v2 - 1]:    # if the edge does not exist
                self.adjMatrix[v1 - 1][v2 - 1] = 1
                self.adjMatrix[v2 - 1][v1 - 1] = 1
                print("Edge added vertex", v1, "and vertex", v2)
            else:  # if the edge exists
                print("Edge already exists vertex", v1, "and vertex", v2)

                                                       # method to remove an edge from the graph
    def remove_e(self, v1, v2):
        if v1 <= self.size and v2 <= self.size:
            if self.adjMatrix[v1 - 1][v2 - 1]:      # if edge exists
                self.adjMatrix[v1 - 1][v2 - 1] = 0
                self.adjMatrix[v2 - 1][v1 - 1] = 0
                print("Edge removed vertex", v1, "and vertex", v2)
            else:
                print("There is no edge vertex", v1, "and vertex", v2)

                                                       # method to print the graph as a matrix
    def print_graph(self):
        print(" ", end="\t")                           # \t to format the matrix
        for i in range(self.size):
            print(i + 1, end="\t")
        print("\n", "-" * (self.size * 5))             # print lines of a matrix
        for i in range(self.size):                     # print each row of the matrix right next to the row
            print(i + 1, "|", end="\t")
            for j in range(self.size):
                print(self.adjMatrix[i][j], end="\t")  # represents an edge between two vertices
            print()


def main():
    g = Graph(7)
    g.add_v(6)
    g.add_e(1, 2)
    g.add_e(2, 3)
    g.add_e(2, 4)
    g.add_e(3, 4)
    g.add_e(4, 5)
    g.add_e(5, 1)
    g.add_e(2, 3)
    g.add_e(1, 7)
    g.remove_e(2, 3)
    print("\n")
    g.print_graph()


if __name__ == '__main__':
    main()
