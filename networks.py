import networkx as nx
G = nx.Graph()

colors = ['Red', 'Blue', 'Green', 'Yellow',  'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']
color = 0
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10])
G.add_edges_from([(1,5),(1,2),(1,8),(2,10),(3,9),
                  (3,1),(3,8),(4,3),(4,5),(4,7),
                  (4,8),(4,10),(4,2),(4,6),(5,1),
                  (5,8),(5,3),(5,7),(5,9),(6,1),(7,6),
                  (7,8),(8,4),(8,1),(9,10),(9,3),(10,1),(10,8),(10,3)])

colors_of_nodes={}


def coloring(node, color):
   for neighbor in G.neighbors(node):
       color_of_neighbor = colors_of_nodes.get(neighbor, None)
       if color_of_neighbor == color:
          return False

   return True

def get_color_for_node(node):
    for color in colors:
       if coloring(node, color):
          return color

def main():
    for node in G.nodes():
        colors_of_nodes[node] = get_color_for_node(node)

    print( colors_of_nodes)


main()
