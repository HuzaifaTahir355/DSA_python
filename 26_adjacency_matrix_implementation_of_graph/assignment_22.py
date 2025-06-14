class Graph:
    def __init__(self, v_no):
        self.vertex_count = v_no
        self.adj_matrix = [[0]*5 for i in range(v_no)]

    def add_edge(self, u, v, weight=1):
        if u <= self.vertex_count and v <= self.vertex_count:
            self.adj_matrix[u][v] = weight
        else:
            raise IndexError("Added value is out of range")

    def remove_edge(self, u, v):
        if self.has_edge(u, v):
            self.adj_matrix[u][v] = 0
        else:
            raise IndexError(f"There is no any edge exist between {u} and {v}")

    def has_edge(self, u, v):
        if u <= self.vertex_count and v <= self.vertex_count:
            if self.adj_matrix[u][v] != 0:
                return True
            else:
                return False
        else:
            raise IndexError("Added value is out of range")

    def print_adj_matrix(self):
        print(self.adj_matrix)


# Testing
g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,0)
g.add_edge(1,4)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(4,1)
g.add_edge(4,2)
g.add_edge(4,3)
g.remove_edge(4,3)
g.print_adj_matrix()


