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

    def assign_color_algorithm1(self):
        for vertex_number in self.id_vertex:
            if self.id_vertex[vertex_number].color == -1:
                suitable_color, number_of_used_colors = self.select_suitable_color(self.id_vertex[vertex_number])
                self.id_vertex[vertex_number].color = suitable_color
                self.check_number_of_used_colors(number_of_used_colors)
                self.paint_adjacency(self.id_vertex[vertex_number])

    def assign_color_algorithm2(self):
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
                    if other_vertex not in self.painted_vertices and vertex_number not in other_vertex.adjacency and self.check_neighbors_color(other_vertex, vertex.color):
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

    def paint_adjacency(self, vertex): # improve this inner loop
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
        with open("outputTest1.txt", "w") as fl:
            fl.write(str(self.number_of_used_colors) + "\n")
            for i in range(1, self.number_of_vertices + 1):
                if i == self.number_of_vertices:
                    fl.write(str(self.id_vertex[i].color))
                    break
                fl.write(str(self.id_vertex[i].color) + " ")

def main():
    management_algorithm1 = Management()
    management_algorithm1.read_problem()
    management_algorithm1.create_vertices()
    management_algorithm1.assign_color_algorithm1()
    chromatic_number_algorithm3 = management_algorithm1.number_of_used_colors

    management_algorithm2 = Management()
    management_algorithm2.read_problem()
    management_algorithm2.create_vertices()
    management_algorithm2.assign_color_algorithm2()
    chromatic_number_algorithm4 = management_algorithm2.number_of_used_colors

    print("Number of used colors for algorithm1:", chromatic_number_algorithm3)
    print("Number of used colors for algorithm2:", chromatic_number_algorithm4)
    selected_chromatic_number = 0
    if chromatic_number_algorithm3 <= chromatic_number_algorithm4:
        management_algorithm1.show_result()
        selected_chromatic_number = chromatic_number_algorithm3
    else:
        management_algorithm2.show_result()
        selected_chromatic_number = chromatic_number_algorithm4
    print("\nSelected chromatic number:", selected_chromatic_number)

main()
