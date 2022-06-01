


# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
 
    # keep track of the color assigned to each vertex
    result = {}
 
    # assign a color to vertex one by one
    for u in range(n):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 
 
# Greedy coloring of a graph
if __name__ == '__main__':
 
    # Add more colors for graphs with many more vertices
    colors = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET']
    cr: int = 0
    # List of graph edges as per the above diagram
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
 
    # total number of nodes in the graph (labelled from 0 to 5)
    n = 6
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # color graph using the greedy algorithm
    colorGraph(graph, n)
 
# Greedy coloring of a graph
if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample1.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    first = f.readline().rsplit(" ")
    print("p:", first[0])  # p
    print("Number of Vertices:", first[1])  # Number of Vertices
    print("Number of Edges:", first[2])  # Number of Edges

    # Create vertices number of given input
    g1 = [[] for i in range(int(first[1]))]

    for i in range(1, int(first[2])):
        temp = f.readline().rsplit(" ")
        g1 = addEdge(g1, int(temp[1]) - 1, int(temp[2]) - 1)
    # color graph using the greedy algorithm
    print("original algorithm:")
    colorGraph(g1, int(first[1]))