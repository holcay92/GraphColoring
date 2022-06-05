def returnToOriginal(current, modifiedList, list_of_colors):
    output_list = []
    # Change the prev original list
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


def addEdge(adjacent_list, vertex, adjacent):
    if not vertex in adjacent_list[adjacent]:
        adjacent_list[vertex].append(adjacent)

    if not vertex in adjacent_list[adjacent]:
        adjacent_list[adjacent].append(vertex)

    return adjacent_list


# Function to assign colors to vertices of a graph
def graph_coloring_1(adjacency_list, number_of_vertices):
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
        color = 0
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

    print("Maximum number of Color is : ", maxColor + 1)
    # print("Colors are : ", color_dict)
    return color_dict, maxColor + 1


# Function to assign colors to vertices of a graph
def graph_coloring_2(adjacency_list, number_of_vertices):
    result = [-1] * number_of_vertices
    result[0] = 0
    available = [False] * number_of_vertices

    # Assign colors to remaining V-1 vertices
    for u in range(1, number_of_vertices):
        for i in adjacency_list[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        cr = 0
        while cr < number_of_vertices:
            # print("cr  : ", cr)
            if available[cr] == False:
                break
            cr += 1
        result[u] = cr

        for i in adjacency_list[u]:
            if result[i] != -1:
                available[result[i]] = False

    maxColor = 0
    for u in range(number_of_vertices):
        if int(result[u]) > maxColor:
            maxColor = int(result[u])

    print("Maximum number of Color is : ", maxColor + 1)
    return result, maxColor + 1



def createOutputFile(colors, maxColor):
    file = open("output3.txt", "w")
    file.write(str(maxColor))
    file.write("\n")
    for i in range(0, len(colors)):
        file.write(str(int(colors[i])))
        file.write(" ")

    file.close()


if __name__ == '__main__':
    # Take the input file into variable
    f = open("sample3.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    header_line = f.readline().rsplit(" ")
    # Create vertices number of given input
    input_list = [[] for i in range(int(header_line[1]))]

    for i in range(1, int(header_line[2]) + 1):
        line = f.readline().rsplit(" ")
        input_list = addEdge(input_list, int(line[1]) - 1, int(line[2]) - 1)

    # Store the original graph in another list
    original_input_list = input_list.copy()
    #print("input_list : ", input_list)
    input_list = sortCrowded(input_list)
    # reverse the 'input_list' in order to make it in descending order
    input_list.reverse()
    modifiedList_binary = fixGraphList(original_input_list, input_list)
    colorList2, min_value_2 = graph_coloring_2(input_list, int(header_line[1]))
    print("min_value_2 : ", min_value_2)
    colorList1, min_value_1 = graph_coloring_1(input_list, int(header_line[1]))
    print("min_value_1 : ", min_value_1)

    min_value = min(min_value_1, min_value_2)
    if min_value_1 < min_value_2:
        colorList = colorList1
    else:
        colorList = colorList2

    output_colors = returnToOriginal(input_list, modifiedList_binary, colorList)
    # print(output_colors)
    createOutputFile(output_colors, min_value)
