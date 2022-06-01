# Python program for solution of M Coloring
# problem using backtracking
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to check if the current color assignment# is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
            return True

    def graphColouring(self, m, colour, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColouring(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
        return False


# A recursive utility function to solve m# coloring problem

def graphColour(self, m, colour, v):
    if v == self.V:
        return True
    for c in range(1, m + 1):
        if self.isSafe(v, colour, c) == True:
            colour[v] = c
            if self.graphColour(m, colour, v + 1) == True:
                return True
            colour[v] = 0
    return False


def graphColouring(self, m):
    colour = [0] * self.V

    if self.graphColourUtil(m, colour, 0) == False:
        return False

    # Print the solutionprint "Solution exist and Following are the assigned colours:"for c in colour:

    return True


# Driver Code
g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.graphColouring(m)


if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample3.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    first = f.readline().rsplit(" ")
    print(first[0])  # p
    print(first[1])  # Number of Vertices
    print(first[2])  # Number of Edges

    # Create vertices number of given input
    g1 = [[] for i in range(int(first[1]))]

    for i in range(1, int(first[2]) + 1):
        temp = f.readline().rsplit(" ")
        g1 = addEdge(g1, int(temp[1]) - 1, int(temp[2]) - 1)