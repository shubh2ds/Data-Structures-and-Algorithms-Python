class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex,":",self.adj_list[vertex])
            print()
    def add_edge(self,V1,V2):
        if V1 in self.adj_list.keys() and V2 in self.adj_list.keys():
            self.adj_list[V1].append(V2)
            self.adj_list[V2].append(V1)
            return True
        return False


obj = Graph()
obj.add_vertex('A')
obj.add_vertex('B')
obj.add_vertex('C')
obj.add_vertex('D')
obj.add_vertex('E')
print("Vertex added!")

obj.add_edge('A','B')
obj.add_edge('B','C')
obj.add_edge('C','D')
obj.add_edge('D','E')
obj.add_edge('E','A')
print("Edges Connected!")
obj.print_graph()



    







                        