class Vertex:

    def __init__(self, id, file_name):
        self.file_name = file_name
        self.id = id
        self.adjacency = []
        self.color = -1  # -1 means it is assigned any color.
        self.degree = -1
        self.read_adjacency()

    def read_adjacency(self):
        with open(self.file_name, "r") as fl: # 245000 * 1000 = 245.000.000 loop
            for line in fl:
                info = line.rsplit(" ")
                if info[0] == 'e' and int(info[1]) == self.id:
                    self.adjacency.append(int(info[2].strip()))
                if info[0] == 'e' and int(info[2]) == self.id:
                    self.adjacency.append(int(info[1].strip()))


        self.degree = len(self.adjacency)


class Management:

    def __init__(self):
        self.file_name = "sample3.txt"
        self.number_of_vertices = 0
        self.number_of_edges = 0
        self.number_of_used_colors = 0
        self.id_vertex = {}
        self.colors = []

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
        #vertices = sorted(temp, key=self.degree)
        #vertices.reverse()
        #del temp
        self.create_id_vertex_dict(temp)
        print("temp: " ,temp)

    def degree(self, vertex):
        return vertex.degree

    def check_number_of_used_colors(self, number_of_used_colors):
        if number_of_used_colors > self.number_of_used_colors:
            self.number_of_used_colors = number_of_used_colors

    def assign_color(self):
        for vertex_number in self.id_vertex:
            suitable_color, number_of_used_colors = self.select_suitable_color(self.id_vertex[vertex_number])
            if self.id_vertex[vertex_number].color == -1:
                self.id_vertex[vertex_number].color = suitable_color
                #print("Vertex " + str(vertex_number) + "  -->  Color " + str(self.id_vertex[vertex_number].color))
                self.check_number_of_used_colors(number_of_used_colors)
                self.paint_adjacency(self.id_vertex[vertex_number])

    def select_suitable_color(self, vertex):
        if vertex.color != -1:
            return -1, -1
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
                #print("Vertex " + str(neighbor.id) + "  -->  Color " + str(neighbor.color))
                self.check_number_of_used_colors(number_of_used_colors)

    def create_id_vertex_dict(self, vertices):
        for vertex in vertices:
            self.id_vertex[vertex.id] = vertex

    def show_result(self):
        print("\nNumber of used colors:", self.number_of_used_colors)

def main():
    management = Management()
    management.read_problem()
    management.create_vertices()
    management.assign_color()
    management.show_result()

main()
