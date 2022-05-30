def addEdge(adj, v, w):
    adj[v].append(w)

    # Note: the graph is undirected
    adj[w].append(v)
    return adj


# Assign colors (starting from 0) to all
# vertices and prints the assignment of colors
def greedyColoring(adj, V):
    result = [-1] * V

    # Assign the first color to first vertex
    result[0] = 0

    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V

    # Assign colors to remaining V-1 vertices
    for u in range(1, V):

        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        cr = 0
        while cr < V:
            if available[cr] == False:
                break

            cr += 1

        # Assign the found color
        result[u] = cr

        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

    # Print the result
    for u in range(V):
        print("Vertex", u+1, " ---> Color", result[u])

    maxColor = 0
    for u in range(V):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor)


# Our sample1.txt file operations
if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample1.txt", encoding='utf-8-sig')

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
    print("g1: \n", g1)
   # g1 = sorted(g1)
    print("g1: \n", g1)
    greedyColoring(g1, int(first[1]))
    g1 = sorted(g1)
    print("After Sorting the list\n")
    greedyColoring(g1, int(first[1]))