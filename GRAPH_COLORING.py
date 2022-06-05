class Vertex:

    def __init__(self, id, file_name):
        self.file_name = file_name
        self.id = id
        self.adjacency = []
        self.color = -1  # -1 means it is assigned any color.
        self.degree = -1
        self.read_adjacency()

    def read_adjacency(self):
        with open(self.file_name, "r") as fl:
            for line in fl:
                info = line.rsplit(" ")
                if info[0] == 'e' and int(info[1]) == self.id and int(info[2].strip()) not in self.adjacency:
                    self.adjacency.append(int(info[2].strip()))
                elif info[0] == 'e' and int(info[2]) == self.id and int(info[1].strip()) not in self.adjacency:
                    self.adjacency.append(int(info[1].strip()))
        self.degree = len(self.adjacency)


class Management:

    def __init__(self):
        self.file_name = "test1.txt"
        self.number_of_vertices = 0
        self.number_of_edges = 0
        self.number_of_used_colors = 0
        self.id_vertex = {}
        self.painted_vertices = {}
        self.colors = []
        self.check_algorithm2 = False

    def read_problem(self):
        with open(self.file_name, "r") as fl:
            p = fl.readline().rsplit(" ")
            self.number_of_vertices = int(p[1])
            self.number_of_edges = int(p[2].strip())
            self.colors = [color for color in range(self.number_of_vertices)]

    def create_vertices(self):
        temp = []
        counter = 0
        if self.number_of_vertices % 2 == 0:
            counter = self.number_of_vertices // 2
        else:
            counter = (self.number_of_vertices // 2) + 1
        start = 1
        end = self.number_of_vertices
        for i in range(counter):
            if self.number_of_vertices % 2 == 1 and i == counter - 1:
                temp.append(Vertex(start, self.file_name))
                break
            temp.append(Vertex(start, self.file_name))
            temp.append(Vertex(end, self.file_name))

            start += 1
            end -= 1
        vertices = sorted(temp, key=self.degree)
        vertices.reverse()
        del temp
        self.create_id_vertex_dict(vertices)

    def degree(self, vertex):
        return vertex.degree

    def check_number_of_used_colors(self, number_of_used_colors):
        if number_of_used_colors > self.number_of_used_colors:
            self.number_of_used_colors = number_of_used_colors

    def graph_coloring_3(self):
        for vertex_number in self.id_vertex:
            if self.id_vertex[vertex_number].color == -1:
                suitable_color, number_of_used_colors = self.select_suitable_color(self.id_vertex[vertex_number])
                self.id_vertex[vertex_number].color = suitable_color
                self.check_number_of_used_colors(number_of_used_colors)
                self.paint_adjacency(self.id_vertex[vertex_number])

    def graph_coloring_4(self):
        self.check_algorithm2 = True
        for vertex_number in self.id_vertex:
            vertex = self.id_vertex[vertex_number]
            if vertex.color == -1:
                suitable_color, number_of_used_colors = self.select_suitable_color(vertex)
                vertex.color = suitable_color
                self.painted_vertices[vertex_number] = vertex
                self.check_number_of_used_colors(number_of_used_colors)
                for vertex_number2 in self.id_vertex:
                    other_vertex = self.id_vertex[vertex_number2]
                    if other_vertex not in self.painted_vertices and vertex_number not in other_vertex.adjacency and self.check_neighbors_color(
                            other_vertex, vertex.color):
                        other_vertex.color = vertex.color
                        self.painted_vertices[vertex_number2] = other_vertex
                        self.check_number_of_used_colors(number_of_used_colors)
        del self.id_vertex

    def select_suitable_color(self, vertex):
        for color in self.colors:
            if self.check_neighbors_color(vertex, color):
                return color, color + 1

    def check_neighbors_color(self, vertex, suitable_color):
        for neighbor_vertex_number in vertex.adjacency:
            neighbor = self.id_vertex[neighbor_vertex_number]
            if neighbor.color == suitable_color:
                return False
        return True

    def paint_adjacency(self, vertex):  # improve this inner loop
        for neighbor_vertex_number in vertex.adjacency:
            neighbor = self.id_vertex[neighbor_vertex_number]
            suitable_color, number_of_used_colors = self.select_suitable_color(neighbor)
            if neighbor.color == -1:
                neighbor.color = suitable_color
                self.check_number_of_used_colors(number_of_used_colors)

    def create_id_vertex_dict(self, vertices):
        for vertex in vertices:
            self.id_vertex[vertex.id] = vertex

    def show_result(self):
        if self.check_algorithm2:
            self.id_vertex = {}
            for i in range(1, self.number_of_vertices + 1):
                self.id_vertex[i] = self.painted_vertices[i]
        with open("output1.txt", "w") as fl:
            fl.write(str(self.number_of_used_colors) + "\n")
            for i in range(1, self.number_of_vertices + 1):
                if i == self.number_of_vertices:
                    fl.write(str(self.id_vertex[i].color))
                    break
                fl.write(str(self.id_vertex[i].color) + " ")


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

    # print("Number of used colors for algorithm1:",maxColor + 1)
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

    # print("Number of used colors for algorithm2:", maxColor + 1)
    return result, maxColor + 1


def createOutputFile(colors, maxColor):
    file = open("output1.txt", "w")
    file.write(str(maxColor))
    file.write("\n")
    for i in range(0, len(colors)):
        file.write(str(int(colors[i])))
        file.write(" ")

    file.close()


if __name__ == '__main__':
    # Take the input file into variable
    f = open("test1.txt", encoding='utf-8-sig')

    # Split the arguments as printed
    header_line = f.readline().rsplit(" ")
    # Create vertices number of given input
    input_list = [[] for i in range(int(header_line[1]))]

    for i in range(1, int(header_line[2]) + 1):
        line = f.readline().rsplit(" ")
        input_list = addEdge(input_list, int(line[1]) - 1, int(line[2]) - 1)

    # Store the original graph in another list
    original_input_list = input_list.copy()
    # print("input_list : ", input_list)
    input_list = sortCrowded(input_list)
    # reverse the 'input_list' in order to make it in descending order
    input_list.reverse()
    modifiedList_binary = fixGraphList(original_input_list, input_list)

    colorList1, min_value_1 = graph_coloring_1(input_list, int(header_line[1]))
    print("Number of used colors for algorithm1:", min_value_1)
    colorList2, min_value_2 = graph_coloring_2(input_list, int(header_line[1]))
    print("Number of used colors for algorithm2:", min_value_2)

    # comparison of 1st and 2nd algorithms
    selected_chromatic_number1 = min(min_value_1, min_value_2)
    print("Selected Chromatic Number1:", selected_chromatic_number1)
    if min_value_1 < min_value_2:
        colorList = colorList1
    else:
        colorList = colorList2
    output_colors = returnToOriginal(input_list, modifiedList_binary, colorList)

    # algo-2
    management_algorithm3 = Management()
    management_algorithm3.read_problem()
    management_algorithm3.create_vertices()
    management_algorithm3.graph_coloring_3()
    chromatic_number_algorithm3 = management_algorithm3.number_of_used_colors

    management_algorithm4 = Management()
    management_algorithm4.read_problem()
    management_algorithm4.create_vertices()
    management_algorithm4.graph_coloring_4()
    chromatic_number_algorithm4 = management_algorithm4.number_of_used_colors
    print("Number of used colors for algorithm3:", chromatic_number_algorithm3)
    print("Number of used colors for algorithm4:", chromatic_number_algorithm4)

    # comparison of 3rd and 4th algorithms
    selected_chromatic_number2 = 0
    if chromatic_number_algorithm3 <= chromatic_number_algorithm4:
        selected_chromatic_number2 = chromatic_number_algorithm3
    else:
        selected_chromatic_number2 = chromatic_number_algorithm4
    print("Selected Chromatic Number2:", selected_chromatic_number2)

    # print("\nSelected chromatic number:", selected_chromatic_number2)

    # final comparison !
    SELECTED_CHROMATIC_NUMBER = 0

    if selected_chromatic_number1 < selected_chromatic_number2:
        SELECTED_CHROMATIC_NUMBER = selected_chromatic_number1
        createOutputFile(output_colors, selected_chromatic_number1)

    elif SELECTED_CHROMATIC_NUMBER == selected_chromatic_number2:
        SELECTED_CHROMATIC_NUMBER = selected_chromatic_number2
        if chromatic_number_algorithm3 <= chromatic_number_algorithm4:
            management_algorithm3.show_result()
        else:
            management_algorithm4.show_result()

    print("SELECTED_CHROMATIC_NUMBER:", SELECTED_CHROMATIC_NUMBER)
