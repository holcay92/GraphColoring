def returnToOrginal(current, modifiedList, colorList):
    output_list = []
    # Change the prev original list
    print("\nOriginal(True) Coloring Order")
    for i in range(0, len(current)):
        # print("vertex : ", modifiedList[i])
        for j in range(0, len(current)):
            # print("komşular ", j, " : ", modifiedList[i][0])
            # print("j : ", j)
            if j == modifiedList[i][0]:
                """print("Color of vertex", j+1, " :", colorList[modifiedList[j][1]])"""
                output_list.append(colorList[modifiedList[j][1]])

    return output_list


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

    #print("arr : ", arr)

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

    return arr


def addEdge(adj, vertex, adjacent):
    if not vertex in adj[adjacent]:
        adj[vertex].append(adjacent)

    # Note: the graph is undirected
    # conditionalAppend(adj, v, w)
    if not vertex in adj[adjacent]:
        adj[adjacent].append(vertex)

    return adj


# Function to assign colors to vertices of a graph
def colorGraph(adjacency_list, number_of_vertices):
    # keep track of the color assigned_colors to each vertex
    result = {}

    # assign a color to vertex one by one
    for u in range(number_of_vertices):
        # check colors of adjacent vertices of `u` and store them in a set
        assigned_colors: list = []
        for i in adjacency_list[u]:
            if i in result:
                if result.get(i) not in assigned_colors:
                    assigned_colors.append(result.get(i))
                    assigned_colors.sort()

        """print("result : ",u,": ", result)
        print("graph[u] : ", adjacency_list[u])
        print("assigned_colors : ", assigned_colors)"""
        # check for the first free color
        color = 1
        for c in assigned_colors:
            if color != c:
                break
            color += 1

        # assign vertex `u` the first available color
        result[u] = color

    """for v in range(number_of_vertices):
        print(f'Color assigned_colors to vertex {v + 1} is {result[v]}')"""

    maxColor = 0
    for u in range(number_of_vertices):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor)

    return result


def createOutputFile(colors, maxColor):
    file = open("output3.txt", "a")
    file.write(str(maxColor))
    file.write("\n")
    for i in range(0, len(colors)):
        file.write(str(int(colors[i])-1))
        file.write(" ")

    file.close()

    # open and read the file after the appending:
    """file = open("output3.txt", "r")
    print(f.read())"""


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
    # g1=sorted(g1)
    # color graph using the greedy algorithm
    #colorGraph(g1, int(first[1]))
    # Store the original graph in another list
    originalG1 = g1.copy()
    g1 = sortCrowded(g1)
    # print("After Sorting the list\n")
    # print("sorted g1: \n", g1)
    #g1_asc = g1
    g1.reverse()
    #print("reversed g1: \n", g1)
    modifiedList_binary = fixGraphList(originalG1, g1)
    print("g1: \n", g1)
    colorList = colorGraph(g1, int(first[1]))
    output_colors = returnToOrginal(g1, modifiedList_binary, colorList)
    print(output_colors)
    #createOutputFile(output_colors, max(output_colors))
    #print("New asceding one: ")
    #colorGraph(g1_asc,  int(first[1]))
