# A class to represent a graph object
import random
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def addEdge(adj, v, w):
    adj[v].append(w)

    # Note: the graph is undirected
    adj[w].append(v)
    return adj


# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
    # keep track of the color assigned to each vertex
    result = {}

    # assign a color to vertex one by one
    for u in range(n):

        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph[u] if i in result])

        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        # assign vertex `u` the first available color
        result[u] = color

    for v in range(n):
        print(f'Color assigned to vertex {v+1} is {result[v]}')

    maxColor = 0
    for u in range(n):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor)


# Greedy coloring of a graph
if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample2.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    first = f.readline().rsplit(" ")
    print(first[0])  # p
    print(first[1])  # Number of Vertices
    print(first[2])  # Number of Edges

    # Create vertices number of given input
    g1 = [[] for i in range(int(first[1]))]

    for i in range(1, int(first[2])):
        temp = f.readline().rsplit(" ")
        g1 = addEdge(g1, int(temp[1]) - 1, int(temp[2]) - 1)
    #g1=sorted(g1)
    # color graph using the greedy algorithm
    colorGraph(g1, int(first[1]))
