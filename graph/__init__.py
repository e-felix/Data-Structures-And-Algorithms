class Vertex:
    """
    Undirected graph implement with Adjacency List
    """

    def __init__(self, value):
        self.value = value
        self.__adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.__adjacent_vertices:
            return

        self.__adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    def depth_first_search(self, vertex, search_value, visited={}):
        if vertex.value == search_value:
            return vertex

        visited[vertex.value] = True

        for v in vertex.__adjacent_vertices:
            if visited.get(v.value):
                continue

            if v.value == search_value:
                return v

            searched_vertex = self.depth_first_search(v, search_value, visited)

            if searched_vertex:
                return searched_vertex

        return None

    def depth_first_search_traverse(self, vertex, visited={}, values=[]):
        visited[vertex.value] = True
        values.append(vertex.value)

        for v in vertex.__adjacent_vertices:
            if visited.get(v.value):
                continue

            self.depth_first_search_traverse(v, visited, values)

        return values

    def breadth_first_search(self, value):
        pass

    def get_all(self):
        return self.depth_first_search_traverse(self)

    def get(self, value):
        return self.depth_first_search(self, value)
