import environment

class Vertex:
    id = 0

    def __init__(self):
        self.adj = []  # A list of vertices this vertex points to
        self.timeCreated = environment.resources["time"]
        self.id = Vertex.id
        Vertex.id += 1


    def add_adjacent(self, other_vertex):
        self.adj.append(other_vertex)

    def remove_adjacent(self, other_vertex):
        self.adj.remove(other_vertex)

    def adjacences(self):
        return self.adj

    def is_adjacent_to(self, other_vertex):
        return other_vertex in self.adj

    def age(self):
        return environment.resources["time"] - self.timeCreated



'''
    The chunks a bug affects are its adjacent vertices
    i.e. if a bug applies to a chunk, add the chunk as an adjacent vertex
'''
class Bug(Vertex):
    def __init__(self, buggy_chunk=None):
        Vertex.__init__(self)
        self.chunks = []
        if buggy_chunk is not None: self.chunks.append(buggy_chunk)

    def affects(self, chunk):
        for affectedChunk in self.chunks:
            if chunk.id == affectedChunk.id:
                return True
        return False


'''
    The bugs a chunk's tests will detect are the adjacent vertices
    i.e. if a chunk detects a bug, add the bug as an adjacent vertex
'''
class Chunk(Vertex):

    def __init__(self, test=None):
        Vertex.__init__(self)
        self.test = test

    def is_tested(self):
        return self.test is not None


'''
    A test that applies to a chunk or series of chunks
    If the test applies to more than one chunk, you should find them in the test's adjacency matrix
'''
class Test(Vertex):

    def __init__(self, chunk=None, works=True):
        Vertex.__init__(self)
        self.chunk = chunk
        self.works = works

