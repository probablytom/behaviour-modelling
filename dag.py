import environment

class Vertex:
    def __init__(self):
        self.adj = []  # A list of vertices this vertex points to
        self.timeCreated = environment.resources["time"]

    def add_adjacent(self, other_vertex):
        self.adj.append(other_vertex)

    def remove_adjacent(self, other_vertex):
        self.adj.remove(other_vertex)

    def adjacences(self):
        return self.adj

    def is_adjacent_to(self, other_vertex):
        return other_vertex in self.adj


'''
    The chunks a bug affects are its adjacent vertices
    i.e. if a bug applies to a chunk, add the chunk as an adjacent vertex
'''
class Bug(Vertex):
    def __init__(self, buggy_chunk=None):
        Vertex.__init__(self)
        if buggy_chunk is not None:
            self.add_adjacent(buggy_chunk)


'''
    The bugs a chunk's tests will detect are the adjacent vertices
    i.e. if a chunk detects a bug, add the bug as an adjacent vertex
'''
class Chunk(Vertex):

    def __init__(self, test=None):
        Vertex.__init__(self)
        if test is not None:
            self.test = test

    def is_tested(self):
        return self.test is not None

    def set_test(self, test):
        self.test = test

    def get_test(self):
        return self.test


'''
    A test that applies to a chunk or series of chunks
    If the test applies to more than one chunk, you should find them in the test's adjacency matrix
'''
class Test(Vertex):

    def __init__(self, chunk=None):
        Vertex.__init__(self)
        if chunk is not None:
            self.chunk = chunk

