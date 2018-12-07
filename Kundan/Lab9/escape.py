class Vertex:
    __slots__ = "id", "connectedTo"

    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def addConnection(self, id, weight):
        self.connectedTo[id] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str(
            [str(x.id) for x in self.connectedTo])


class Graph:
    __slots__ = "vertices", "size"

    def __init__(self):
        self.vertices = {}
        self.size = 0

    def getVertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def addVertex(self, id):
        if self.getVertex(id) is None:
            vertex = Vertex(id)
            self.vertices[id] = vertex
            self.size += 1
            return vertex
        else:
            return self.getVertex(id)

    def addEdge(self, src, dest, cost=0):
        if src not in self.vertices:
            self.addVertex(src)
        if dest not in self.vertices:
            self.addVertex(dest)
        self.vertices[src].addConnection(self.vertices[dest], cost)


def findShortestPath(start, end):
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
    return str(y) + "," + str(x)


def createGraph(pond, rowSize, columnSize):
    graph = Graph()
    for x in range(0, rowSize):
        for y in range(0, columnSize):
            if pond[x][y] != "*":
                src = makeVertexName(x, y)
                graph.addVertex(src)

                if y != columnSize - 1:
                    # go right
                    rockIndex = -1
                    for k in range(y + 1, columnSize):
                        if pond[x][k] == "*":
                            rockIndex = k
                            break
                    if rockIndex != -1:
                        dest = makeVertexName(x, rockIndex - 1)
                    else:
                        dest = makeVertexName(x, columnSize - 1)
                    graph.addEdge(src, dest)

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
    escapes = {}
    for src in graph.vertices.keys():
        if src == exitVertex:
            steps = 1
        else:
            steps = findShortestPath(graph.getVertex(src), graph.getVertex(
                exitVertex))
        if steps is None:
            key = -1
        else:
            key = steps
        try:
            escapes[key].append(src)
        except KeyError:
            escapes[key] = [src]
    for key in range(1, graph.size + 1):
        if key in escapes:
            print(key, " : ", escapes[key])
    if -1 in escapes:
        print("Not Reachable : ", escapes[-1])


def main():
    filenames = ["test1.txt", "test2.txt", "test3.txt"]
    for filename in filenames:
        print("Testing", filename)
        rowSize = 0
        columnSize = 0
        exitRow = -1
        pond = []
        with open(filename) as f:
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
        for x in range(0, rowSize):
            for y in range(0, columnSize):
                print(pond[x][y], end=" ")
            print()
        graph = createGraph(pond, rowSize, columnSize)
        exitVertex = makeVertexName(exitRow, columnSize-1)
        printExitPaths(graph, exitVertex)
        print("\n")

if __name__ == '__main__':
    main()