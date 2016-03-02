class Vertex:
    def __init__(self):
        self.adj = []  # A list of vertices this vertex points to

    def add_adjacent(self, other_vertex):
        self.adj.add(other_vertex)

    def remove_adjacent(self, other_vertex):
        self.adj.remove(other_vertex)

    def adjacences(self):
        return self.adj

'''
    The chunks a bug affects are its adjacent vertices
    i.e. if a bug applies to a chunk, add the chunk as an adjacent vertex
'''
class Bug(Vertex):
    pass

'''
    The bugs a chunk's tests will detect are the adjacent vertices
    i.e. if a chunk detects a bug, add the bug as an adjacent vertex
'''
class Chunk(Vertex):

    def __init__(self):
        Vertex.__init__(self)
        self.tested = False
        self.detects = []

    def is_tested(self):
        return self.tested

    def set_tested(self, tested):
        self.tested = tested