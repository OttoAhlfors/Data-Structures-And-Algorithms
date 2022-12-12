# Lähteet:
# https://favtutor.com/blogs/floyd-warshall-algorithm

from graph import Graph


def floyd(graph):
    # Tehdään uusi palautettavaa graafi
    dist = graph.graph_matrix.copy()

    # Tehdään palautettavan graafin mahdottomista reiteistä 
    # functionaalisesti loputtoman pituisia
    i = 0
    for r in dist:
        i = i + 1
        x = 0
        for p in dist[i - 1]:
            x = x + 1 
            if dist[i - 1][x - 1] == 0 and i != x:
                dist[i - 1][x - 1 ] = 999

    # Floydin algoritmi
    for r in range(graph.vertex_count):
        for p in range(graph.vertex_count):
            for q in range(graph.vertex_count):
                    dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])

    # Merkitään mahdottomat reitit nollaksi
    i = 0
    for r in dist:
        i = i + 1
        x = 0
        for p in dist[i - 1]:
            x = x + 1 
            if dist[i - 1][x - 1] == 999:
                dist[i - 1][x - 1 ] = 0

    return dist
    

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
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 