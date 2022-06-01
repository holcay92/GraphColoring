class Graph(object):
    def __init__(self, adjacency_list, isColored, degree, color):
        self.adjacency_list = adjacency_list
        self.isColored = isColored
        self.degree = degree
        self.color = color



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


def add_adjacent_vertices(adjacency_list, vertex, adjacent):
    if vertex + 1 not in adjacency_list[adjacent]:
        adjacency_list[vertex].append(adjacent + 1)
    if vertex + 1 not in adjacency_list[adjacent]:
        adjacency_list[adjacent].append(vertex + 1)
    # print(adjacency_list)
    return adjacency_list


def greedyColoring(newlist, number_of_vertices):
    color = [-1] * number_of_vertices
    color[0] = 0
    cr = 0

    for i in range(1, number_of_vertices):

        for j in range(i+1, number_of_vertices):
            if i not in newlist[i]:
                color[i] = cr
        cr += 1

    print("color:",color)



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
    vertex_list = [int(first[1])]

    for i in range(1, int(first[2]) + 1):
        temp = f.readline().rsplit(" ")
        # Add adjacent vertices to the list of the vertices
        g1 = add_adjacent_vertices(g1, int(temp[1]) - 1, int(temp[2]) - 1)

    # Prints the adjacency list but not index.
    print("g1:", g1)
    degree_list = [0] * int(first[1])
    reversed_g1: list = g1
    reversed_g1 = sortCrowded(reversed_g1)
    reversed_g1.reverse()
    print("reversed_g1:", reversed_g1)
    # Calculate the degree of each vertex
    for i in range(len(g1)):
        degree_list[i] = len(g1[i])
    print("degree list", degree_list)

    templist = degree_list.copy()
    templist.sort(reverse=True)
    max_val_index = min(enumerate(g1), key=lambda tup: len(tup[1]))


    newlist = fixGraphList(g1, reversed_g1)
    greedyColoring(newlist, int(first[1]))
    print(newlist)
