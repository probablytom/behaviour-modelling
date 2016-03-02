class Vertex:
    def __init__(self):
        self.adj = []  # A list of vertices this vertex points to

    def add_adjacent(self, other_vertex):
        self.adj.add(other_vertex)

    def remove_adjacent(self, other_vertex):
        self.adj.remove(other_vertex)

    def adjacences(self):
        return self.adj

class Bug(Vertex):
    pass

class Chunk(Vertex):

    def __init__(self):
        super(Vertex, self).__init__()
        self.tested = False

    def is_tested(self):
        return self.tested

    def set_tested(self, tested):
        self.tested = tested

