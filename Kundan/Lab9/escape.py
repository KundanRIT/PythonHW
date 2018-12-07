"""
Author: Kundan Kumar (kk7272) & Deepam Shah (ds3689)
Lab 9 - reads in a maze from a file, constructs a graph,
finds out from which squares we can escape with shortest number of steps.
"""

class Vertex:
    """
    Vertex Data Structure. Implements vertex id and its neighboring connections
    Used Lecture Code from https://www.cs.rit.edu/~csci603/Lectures/13/vertex.py
    """
    __slots__ = "id", "connectedTo"

    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def addConnection(self, id, weight):
        """
        Adding new connection
        :param id:
        :param weight:
        :return: None
        """
        self.connectedTo[id] = weight

    def getConnections(self):
        """
        Fetching all available connections of the vertex
        :return: None
        """
        return self.connectedTo.keys()


class Graph:
    """
    Directed Graph Data Structure. Implements adding vertices and edges.
    Used Lecture Code from https://www.cs.rit.edu/~csci603/Lectures/13/graph.py
    """
    __slots__ = "vertices", "size"

    def __init__(self):
        self.vertices = {}
        self.size = 0

    def getVertex(self, id):
        """
        Returns the vertex with the given id.
        :param id: id of vertex
        :return: Vertex if present. None otherwise
        """
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def addVertex(self, id):
        """
        Add a new vertex and return it. If vertex is already present, do not
        create a new vertex.
        :param id:
        :return: Vertex
        """
        if self.getVertex(id) is None:
            vertex = Vertex(id)
            self.vertices[id] = vertex
            self.size += 1
            return vertex
        else:
            return self.getVertex(id)

    def addEdge(self, src, dest, cost=0):
        """
        Add edge between source and destination vertices
        :param src:
        :param dest:
        :param cost:
        :return: None
        """
        if src not in self.vertices:
            self.addVertex(src)
        if dest not in self.vertices:
            self.addVertex(dest)
        self.vertices[src].addConnection(self.vertices[dest], cost)


def findShortestPath(start, end):
    """
    Graph BFS algorithm to calculate number of steps required for any cell to reach the exit vertex.
    Used lecture code from https://www.cs.rit.edu/~csci603/Lectures/13
    /searchAlgos.py modifying the method findShortestPath to return the
    number of stepssteps
    :param start: start vertex
    :param end: exit vertex
    :return: shortest number of steps taken by cell to exit the pond. None if not reachable.
    """
    queue = [start]
    predecessors = {start: None}
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
            if neighbor not in predecessors:
                predecessors[neighbor] = current
                queue.append(neighbor)
    if end in predecessors:
        current = end
        steps = 0
        while current != start:
            steps += 1
            current = predecessors[current]
        return steps
    else:
        return None


def makeVertexName(x, y):
    """
    Generates the vertex name using the cell index
    :param x: row index
    :param y: column index
    :return: vertex name
    """
    return str(y) + "," + str(x)


def createGraph(pond, rowSize, columnSize):
    """
    Creates a directed graph using the given pond matrix
    :param pond:
    :param rowSize:
    :param columnSize:
    :return: directed graph
    """
    graph = Graph()
    for x in range(0, rowSize):
        for y in range(0, columnSize):
            if pond[x][y] != "*": # vertex for cell with a rock is not required
                src = makeVertexName(x, y)
                graph.addVertex(src)

                #possible path towards the right side of the cell
                if y != columnSize - 1:
                    # go right
                    rockIndex = -1
                    for k in range(y + 1, columnSize):
                        if pond[x][k] == "*":
                            rockIndex = k
                            break
                    # if rock is found in the path, then connect the vertex
                    # with cell prior to the rock otherwise, to the end of
                    # path
                    if rockIndex != -1:
                        dest = makeVertexName(x, rockIndex - 1)
                    else:
                        dest = makeVertexName(x, columnSize - 1)
                    graph.addEdge(src, dest) # make connection

                #possible path towards the left side of the cell
                if y != 0:
                    # go left
                    rockIndex = -1
                    for k in range(y - 1, -1, -1):
                        if pond[x][k] == "*":
                            rockIndex = k
                            break
                    if rockIndex != -1:
                        dest = makeVertexName(x, rockIndex + 1)
                    else:
                        dest = makeVertexName(x, 0)
                    graph.addEdge(src, dest)

                #possible path going below the current cell
                if x != rowSize - 1:
                    # go down
                    rockIndex = -1
                    for k in range(x + 1, rowSize):
                        if pond[k][y] == "*":
                            rockIndex = k
                            break
                    if rockIndex != -1:
                        dest = makeVertexName(rockIndex - 1, y)
                    else:
                        dest = makeVertexName(columnSize - 1, y)
                    graph.addEdge(src, dest)

                #possible path going above the current cell
                if x != 0:
                    # go up
                    rockIndex = -1
                    for k in range(x - 1, -1, -1):
                        if pond[k][y] == "*":
                            rockIndex = k
                            break
                    if rockIndex != -1:
                        dest = makeVertexName(rockIndex + 1, y)
                    else:
                        dest = makeVertexName(0, y)
                    graph.addEdge(src, dest)
    return graph


def printExitPaths(graph, exitVertex):
    """
    Displays the cells and shortest number of steps taken by the cell to
    reach exit
    :param graph: directed graph of the pond
    :param exitVertex: vertex of the exit cell
    :return: None
    """
    escapes = {} # store escaping vertex and steps taken as key value pair in
    #  a dictionary
    for src in graph.vertices.keys():
        if src == exitVertex:
            steps = 1
        else:
            steps = findShortestPath(graph.getVertex(src), graph.getVertex(
                exitVertex))
        if steps is None:
            key = -1 # store unreachable cells with -1
        else:
            key = steps
        try:
            escapes[key].append(src)
        except KeyError:
            escapes[key] = [src] # initialize new key
    for key in range(1, graph.size + 1): # number of steps cannot be more
        # than the number of vertices in the grap
        if key in escapes:
            print(key, " : ", escapes[key])
    if -1 in escapes:
        print("Not Reachable : ", escapes[-1])


def main():
    """
    Main Method.
    :return: None
    """
    filenames = ["test1.txt", "test2.txt", "test3.txt"]
    for filename in filenames:
        print("Testing", filename)
        rowSize = 0
        columnSize = 0
        exitRow = -1
        pond = []
        with open(filename) as f:
            # read test files one by one
            firstLineRead = False
            for line in f:
                if not firstLineRead:
                    rowSize, columnSize, exitRow = line.strip().split()
                    rowSize = int(rowSize)
                    columnSize = int(columnSize)
                    exitRow = int(exitRow)
                    firstLineRead = True
                else:
                    pond.append(line.strip().split())
        # print pond
        for x in range(0, rowSize):
            for y in range(0, columnSize):
                print(pond[x][y], end=" ")
            print()
        # create graph for the pond
        graph = createGraph(pond, rowSize, columnSize)
        exitVertex = makeVertexName(exitRow, columnSize-1)
        # print reachable and unreachable cells
        printExitPaths(graph, exitVertex)
        print("\n")

if __name__ == '__main__':
    main()