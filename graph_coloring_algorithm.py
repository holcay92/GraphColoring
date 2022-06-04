# CSE2046 - Analysis of Algorithms
# Homework  2 Report
# Group Members
# 150119639 - Erdem PEHLİVANLAR
# 150120056 - Haldun Halil OLCAY
# 170517033 - YasinAlper BİNGÜL


def returnToOriginal(current, modifiedList, list_of_colors):
    output_list = []
    # Change the prev original list
    print("\nOriginal(True) Coloring Order")
    for i in range(0, len(current)):
        for j in range(0, len(current)):
            if j == modifiedList[i][0]:
                output_list.append(list_of_colors[modifiedList[j][1]])
    return output_list


def sortCrowded(list_of_adjacents):
    list_of_sorted_adjacents = sorted(list_of_adjacents, key=len)
    return list_of_sorted_adjacents


def fixGraphList(previous_list, current_list):
    prevIndex = 0
    currIndex = 0
    modified_list = [[0] * 2 for i in range(len(previous_list))]

    # Determine which vertex must be change with which vertex
    for i in range(0, len(previous_list)):
        prevIndex = i
        for j in range(0, len(previous_list)):
            # Search the same list in the adj list
            if previous_list[i] == current_list[j]:
                currIndex = j
                break

        modified_list[i][0] = prevIndex
        modified_list[i][1] = currIndex

    # Change the prev original list
    for i in range(0, len(current_list)):
        for j in range(0, len(current_list[i])):
            for z in range(0, len(current_list)):
                if current_list[i][j] == modified_list[z][0]:
                    current_list[i][j] = modified_list[z][1]
                    break
    return modified_list


def addEdge(adj, vertex, adjacent):
    if not vertex in adj[adjacent]:
        adj[vertex].append(adjacent)
    if not vertex in adj[adjacent]:
        adj[adjacent].append(vertex)

    return adj


# Function to assign colors to vertices of a graph
def graph_coloring(adjacency_list, number_of_vertices):
    # keep track of the color assigned_colors to each vertex
    color_dict = {}

    # assign a color to vertex one by one
    for index in range(number_of_vertices):
        # keeping colors of adjacent vertices in a list
        assigned_colors: list = []
        for i in adjacency_list[index]:
            if i in color_dict:
                if color_dict.get(i) not in assigned_colors:
                    assigned_colors.append(color_dict.get(i))
                    assigned_colors.sort()

        # check for an available color
        color = 1
        for c in assigned_colors:
            if color != c:
                break
            color += 1

        # give vertex `index` the first available color
        color_dict[index] = color

    maxColor = 0
    for index in range(number_of_vertices):
        if int(color_dict[index]) > maxColor:
            maxColor = int(color_dict[index])

    print("Maximum number of Color is : ", maxColor)
    return color_dict


def createOutputFile(colors, maxColor):
    file = open("output3.txt", "w")
    file.write(str(maxColor))
    file.write("\n")
    for i in range(0, len(colors)):
        file.write(str(int(colors[i]) - 1))
        file.write(" ")
    file.close()


if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample3.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    header_line = f.readline().rsplit(" ")
    # Create vertices number of given input
    input_list = [[] for i in range(int(header_line[1]))]

    for i in range(1, int(header_line[2])):
        temp = f.readline().rsplit(" ")
        input_list = addEdge(input_list, int(temp[1]) - 1, int(temp[2]) - 1)

    # Store the original graph in another list
    original_input_list = input_list.copy()
    input_list = sortCrowded(input_list)
    # reverse the 'input_list' in order to make it in descending order
    input_list.reverse()
    modifiedList_binary = fixGraphList(original_input_list, input_list)
    colorList = graph_coloring(input_list, int(header_line[1]))
    output_colors = returnToOriginal(input_list, modifiedList_binary, colorList)
    print(output_colors)
    createOutputFile(output_colors, max(output_colors))


