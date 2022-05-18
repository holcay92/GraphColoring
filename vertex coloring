def isSafeToColor(graph, color):
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] == 1 and color[j] == color[i]:
                return False
    return True
 
 
def printColorArray(color):
    print("Solution colors are: ")
    for i in range(len(color)):
        print(color[i], end=" ")
 
 
def graphColoring(graph, m, i, color):
    if i == V:
        if isSafeToColor(graph, color):
            printColorArray(color)
            return True
        return False
 
    for j in range(1, m + 1):
        color[i] = j
        if graphColoring(graph, m, i + 1, color):
            return True
 
        color[i] = 0
 
    return false
