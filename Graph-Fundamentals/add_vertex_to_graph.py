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


obj = Graph()
obj.add_vertex('A')
obj.add_vertex('B')
obj.add_vertex('C')
obj.add_vertex('D')
obj.add_vertex('E')
obj.print_graph()



    







                        