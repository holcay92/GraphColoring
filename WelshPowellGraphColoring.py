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


def welshPowell(adj, num_of_ver):
    indicator = 0
    color = [-1] * num_of_ver

    c = 0
    for x in range(0, num_of_ver):
        if color[x] == -1:
            # print("Girdi for x: ", x)
            # print("color : ", c)
            color[x] = c
            index = x

            for u in range(1, num_of_ver):
                # print("vertex : ", u)
                for i in adj[u]:
                    # print("komşu : ", i)
                    if i == index:
                        indicator = 1

                if indicator == 0 and color[u] == -1:
                    # print("boyandı")
                    color[u] = c
                    # print("")
                else:
                    # print("not boyanmadı")
                    indicator = 0
                    # print(" ")
            # print("color :", color)
            # print(" ")
            c += 1
        #else:
            # print("atla")

    print("color :", color)
    maxColor = 0
    for u in range(num_of_ver):
        if int(color[u]) > maxColor:
            maxColor = int(color[u])

    print("Maximum number of Color is : ", maxColor + 1)


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

    for i in range(1, int(first[2]) + 1):
        temp = f.readline().rsplit(" ")
        g1 = addEdge(g1, int(temp[1]) - 1, int(temp[2]) - 1)

    # Store the original graph in another list
    originalG1 = g1
    print("original g1: \n", originalG1)
    g1 = sortCrowded(g1)
    g1.reverse()
    fixedSorted = fixGraphList(originalG1, g1)
    print("fixed g1: \n", fixedSorted)

    welshPowell(fixedSorted, int(first[1]))
