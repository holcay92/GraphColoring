# A class to represent a graph object
import random


class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def sortCrowded(adj):
    adj2 = sorted(adj, key=len)
    return adj2

def fixGraphList(previous, current):
    prevIndex = 0
    currIndex = 0
    arr = [[0] * 2 for i in range(len(previous))]

    # Determine which vertex must be change with which vertex
    for i in range(0, len(previous)):
        prevIndex = i
        for j in range(0, len(previous)):
            # Search the same list in the adj list
            if previous[i] == current[j]:
                currIndex = j
                break

        arr[i][0] = prevIndex
        arr[i][1] = currIndex

    print("arr : ", arr)

    # Change the prev original list
    for i in range(0, len(current)):
        # print("ilgili b : ", current[i])
        for j in range(0, len(current[i])):
            # print("komşular ", j, " : ", current[i][j])

            for z in range(0, len(current)):
                # print("karşılaştır ", arr[z][0])
                if current[i][j] == arr[z][0]:
                    # print("exist")
                    current[i][j] = arr[z][1]
                    break
                # else:
                    # print("not exist")
            # print(" ")

        # print(" ")
        # print(" ")

    return current


def addEdge(adj, vertex, adjacent):
    if not vertex in adj[adjacent]:
        adj[vertex].append(adjacent)

    # Note: the graph is undirected
    # conditionalAppend(adj, v, w)
    if not vertex in adj[adjacent]:
        adj[adjacent].append(vertex)

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
        print(f'Color assigned to vertex {v + 1} is {result[v]}')

    maxColor = 0
    for u in range(n):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor)


# Greedy coloring of a graph
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

    for i in range(1, int(first[2])):
        temp = f.readline().rsplit(" ")
        g1 = addEdge(g1, int(temp[1]) - 1, int(temp[2]) - 1)
    # g1=sorted(g1)
    # color graph using the greedy algorithm
    colorGraph(g1, int(first[1]))
    # Store the original graph in another list
    originalG1 = g1
    g1 = sortCrowded(g1)
    # print("After Sorting the list\n")
    # print("sorted g1: \n", g1)
    g1.reverse()
    print("reversed g1: \n", g1)
    a = fixGraphList(originalG1, g1)
    print("fixed g1: \n", a)
    colorGraph(a, int(first[1]))
