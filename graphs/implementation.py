class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Create link between the 2 vertices
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                # Delete link between the 2 vertices
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                # Delete all other links from other vertices to target vertex
                self.adj_list[other_vertex].remove(vertex)
            # Delete the target vertex
            del self.adj_list[vertex]

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

graph.print_graph()

graph.remove_edge("A", "B")
graph.print_graph()

graph.remove_vertex("D")
graph.print_graph()
