#Lähteet:
# https://moodle.lut.fi/mod/page/view.php?id=816182
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
from graph import Graph

def dijkstragraph(graph, start):
    # Tehdään uusi palautettavaa graafi
    N = graph.vertex_count
    matrix = [[0] * N for i in range(N)]
    new_graph = Graph(matrix)

    # Tehdään lista, johon tallennetaan lyhimmät etäisyydet
    # Alustavasti kaikkiin solmuihin on 9999 matka
    dist = [9999] * graph.vertex_count

    # Aloitus solmuun on etäisyys aina 0
    dist[start] = 0

    # Pidetään kirjaaa käytdyistä solmuista
    visited = [False] * graph.vertex_count

    # Käydään läpi kaikki solmut
    for i in range(graph.vertex_count):
        min = 9999
        min_index = 0
        # Etsitään lyhin reitti
        for j in range(graph.vertex_count):
            if dist[j] < min and visited[j] == False:
                min = dist[j]
                min_index = j

        u = min_index

        visited[u] = True

        # Käydään läpi kaikki solmun naapurit
        for v in range(graph.vertex_count):
            # Jos solmuun on reitti ja sen luona ei ole käyty
            if graph.weight(u, v) > 0 and visited[v] == False and dist[v] > dist[u] + graph.weight(u, v):
                # Etäisyys solmuun on sama kuin edelliseen solmuun + uuden solmun paino
                dist[v] = dist[u] + graph.weight(u, v)
                # Tallennetaan uusi paino uuteen graafiin
                print("u: ", u, "v: ", v, "weight: ", graph.weight(u, v))
                new_graph.graph_matrix[u][v] = graph.weight(u, v)
    
    print(dist)
    print()
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