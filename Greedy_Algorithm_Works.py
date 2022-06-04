def fixGraphList(previous, current):
    prevIndex = 0
    currIndex = 0
    modifiedList = [[0] * 2 for i in range(len(previous))]

    # Determine which vertex must be change with which vertex
    for i in range(0, len(previous)):
        prevIndex = i
        for j in range(0, len(previous)):
            # Search the same list in the adj list
            if previous[i] == current[j]:
                currIndex = j
                break

        modifiedList[i][0] = prevIndex
        modifiedList[i][1] = currIndex

    print("modifiedList : ", modifiedList)

    # Change the prev original list
    for i in range(0, len(current)):
        # print("ilgili b : ", current[i])
        for j in range(0, len(current[i])):
            # print("komşular ", j, " : ", current[i][j])

            for z in range(0, len(current)):
                # print("karşılaştır ", modifiedList[z][0])
                if current[i][j] == modifiedList[z][0]:
                    # print("exist")
                    current[i][j] = modifiedList[z][1]
                    break
                # else:
                # print("not exist")
            # print(" ")

        # print(" ")
        # print(" ")

    return modifiedList


def returnToOrginal(current, modifiedList, colorList):
    # Change the prev original list
    for i in range(0, len(current)):
        # print("vertex : ", modifiedList[i])
        for j in range(0, len(current)):
            # print("komşular ", j, " : ", modifiedList[i][0])
            # print("j : ", j)
            if j == modifiedList[i][0]:
                print("Color of vertex", j+1, " :", colorList[modifiedList[j][1]])

            # print(" ")
        # print("")


def sortCrowded(adj):
    adj2 = sorted(adj, key=len)
    return adj2


def addEdge(adj, vertex, adjacent):
    if not vertex in adj[adjacent]:
        adj[vertex].append(adjacent)

    # Note: the graph is undirected
    # conditionalAppend(adj, v, w)
    if not vertex in adj[adjacent]:
        adj[adjacent].append(vertex)

    return adj


# Assign colors (starting from 0) to all
# vertices and prints the assignment of colors
def greedyColoring(g1, V):
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
        # print("Result begin : ", result)
        for i in g1[u]:
            # print("Available: ", available)
            if result[i] != -1:
                available[result[i]] = True

        # print("Result  : ", result)

        # Find the first available color
        cr = 0
        while cr < V:
            # print("cr  : ", cr)
            if available[cr] == False:
                break

            cr += 1

        # Assign the found color
        # print("res cr  : ", cr)
        result[u] = cr

        # print("New Result  : ", result)
        # print(" ")

        # Reset the values back to false
        # for the next iteration
        for i in g1[u]:
            if result[i] != -1:
                available[result[i]] = False

    # Print the result
    for u in range(V):
        print("Vertex", u + 1, " ---> Color", result[u])

    maxColor = 0
    for u in range(V):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor + 1)

    return result


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
    print("g1: \n", g1)
    colorList = greedyColoring(g1, int(first[1]))

    # Store the original graph in another list
    originalG1 = g1

    g1 = sortCrowded(g1)
    # print("After Sorting the list\n")
    # print("sorted g1: \n", g1)
    g1.reverse()
    print("reversed g1: \n", g1)
    modifiedList_binary = fixGraphList(originalG1, g1)
    print("fixed g1: \n", g1)
    colorList = greedyColoring(g1, int(first[1]))
    returnToOrginal(g1,modifiedList_binary, colorList)

    