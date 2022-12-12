#Lähteet:
# https://moodle.lut.fi/mod/page/view.php?id=816182
# https://moodle.lut.fi/mod/page/view.php?id=694947
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


class Graph:
    def __init__(self, graph_matrix):
        self.graph_matrix = graph_matrix
        #self.graph_list = [[] for i in range(len(graph_matrix))]
        self.vertex_count = len(graph_matrix)
        self.edge_count = 9

    # Depth first search
    def df_printUtil(self, vertex, visited):
        visited[vertex] = True
        print(vertex, "", end="")

        for i in range(self.vertex_count):
            if visited[i] == False and self.weight(vertex, i) != -1:
                self.df_printUtil(i, visited)

    def df_print(self, start_vertex):
        visited = [False] * self.vertex_count

        self.df_printUtil(start_vertex, visited)
        print()

    # Breadth first search
    def bf_print(self, start_vertex):
        visited = [False] * self.vertex_count
        que = []

        que.append(start_vertex)
        visited[start_vertex] = True

        while que:
            vertex = que.pop(0)
            print(vertex, "", end="")

            for i in range(self.vertex_count):
                if visited[i] == False and self.weight(vertex, i) != -1:
                    que.append(i)
                    visited[i] = True
        print()

    # Weigth
    def weight(self, start_vertex, end_vertex):
        weight = self.graph_matrix[start_vertex][end_vertex]
        if weight == 0:
            return -1
        return self.graph_matrix[start_vertex][end_vertex]


if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    
    graph = Graph(matrix)

    graph.df_print(0)           # 0 2 1 3 5 4      
    graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1