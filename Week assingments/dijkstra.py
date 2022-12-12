#Lähteet:
# https://moodle.lut.fi/mod/page/view.php?id=816182
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
from graph import Graph

def dijkstragraph(graph, start):
    # Tehdään uusi palautettavaa graafi
    N = graph.vertex_count
    matrix = [[0] * N for i in range(N)]
    new_graph = Graph(matrix)

    
    return new_graph
    
 

if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        ]

    graph = Graph(matrix)

    new_graph = dijkstragraph(graph, 0)

    # Testi printti
    N = new_graph.vertex_count
    for i in range(N):
        for j in range(N):
            print(f"{new_graph.graph_matrix[i][j]:3d}", end="")
        print()
    print()

    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8 
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    print(new_graph.weight(3, 6))   # 4
    print(new_graph.weight(5, 8))   # -1