def conditionalAppend(adj, v, w):
    if v not in adj[w]:
        adj[w].append(v)


def sortCrowded(adj):
    adj2 = sorted(adj, key=len)
    return adj2


""" if not vertex in adj[adjacent]:
        adj[vertex].append(adjacent)

    # Note: the graph is undirected
   
    if not vertex in adj[adjacent]:
        adj[adjacent].append(vertex)
    return adj   """


def addEdge(adj, vertex, adjacent):
    if vertex not in adj[adjacent]:
        adj[vertex].append(adjacent)
    if vertex not in adj[adjacent]:
        adj[adjacent].append(vertex)

    return adj


# Assign colors (starting from 0) to all
# vertices and prints the assignment of colors
def greedyColoring(adj, V, max_val_index):
    result = [-1] * V

    # Assign the first color to first vertex
    result[max_val_index] = 0

    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V

    # Assign colors to remaining V-1 vertices
    for u in range(0, V):

        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:

            if result[i] != -1:
               # print("Color ", result[i], " is unavailable for vertex ", u)
                available[result[i]] = True

        # Find the first available color
        cr = 0
        while cr < V:
            if available[cr] == False:
                break

            cr += 1

        # Assign the found color

       # print("cr: ", cr)
        result[u] = cr

        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

    # Print the result
    #for u in range(V):
     #   print("Vertex", u + 1, " ---> Color", result[u])

    maxColor = 0
    for u in range(V):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor + 1)


# Our sample1.txt file operations
if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample.txt", encoding='utf-8-sig')

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

    #print("original g1: \n", g1)
    max_val_index = min(enumerate(g1), key=lambda tup: len(tup[1]))
    maxLen = min(len(p) for p in g1)
    print("original g1 max element len : \n", len(g1[531]))

    greedyColoring(g1, int(first[1]), max_val_index[0])

    g1 = sortCrowded(g1)
   # print("After Sorting the list\n")
    #print("g1: \n", g1)
    g1.reverse()
    print("reversed g1 max element len : \n", len(g1[0]))

   # greedyColoring(g1, int(first[1]))
print("max len",maxLen)
print("max index:", max_val_index[0])

