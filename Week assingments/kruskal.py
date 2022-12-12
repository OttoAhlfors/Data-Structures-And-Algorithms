# Lähteet:
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

from graph import Graph

def sort(list):
    return list[2]

# Etsitään avaimen juurisolmu
def findParent(mst, parent, i):
    # Jos avain on juurisolmu niin palautetaan se 
    if parent[i] != i:
        # Muuten etsitään juurisolmu rekursiolla
        parent[i] = findParent(mst, parent, parent[i])
    return parent[i]

# Yhdistetään avaimet toisiinsa
def heritage(parent, rank, n, m):
    
    # Jos ensimmäinen avain on pienempi niin se yhdistetään toiseen
    if rank[n] < rank[m]:
        parent[n] = m
    elif rank[n] > rank[m]:
        parent[n] = n

    # Jos avaimet ovat samanarvoisia niin lisätään toinen
    else:
        parent[m] = n
        rank[n] += 1

def kruskal(graph):

    # Tehdään tyhjä mst graaafi
    N = graph.vertex_count
    matrix = [[0] * N for i in range(N)]
    mst = Graph(matrix)

    minHeap = []

    # Kaksi listaa joihin tallennetaan käytyjen alkoiden yhteyksiö
    parent = []
    rank = []

    # Alustetaan listat
    for node in range(graph.vertex_count):
        parent.append(node)
        rank.append(0)

    # Laitetaan kaikki yhteydet listaan
    for i in range(graph.vertex_count):
        for j in range(graph.vertex_count):
            # Jos paino on -1 niin yhteuttä ei ole
            if graph.weight(i, j) != -1:
                minHeap.append([i, j, graph.weight(i, j)])

    # Järjestetään lista pienimmästä suurimpaan
    minHeap.sort(key=sort)

    # Käydään läpi kaikki yhteydet pienimmästä suurimpaan
    edges = 0
    x = 0

    # Tarvittavien yhteyksien määrä on solmujen määrä - 1
    while edges < graph.vertex_count - 1:
        i = minHeap[x]
        x += 1
        weight = i[2]
        vertex1 = i[0]
        vertex2 = i[1]

        # Etsitään yhteyden alkupisteiden juurisolmut
        n = findParent(graph, parent, vertex1)
        m = findParent(graph, parent, vertex2)

        if n != m:
            print(i)
            # Lisätään yhteys mst graafiin kumpaankin suuntaan
            edges += 1
            mst.graph_matrix[vertex1][vertex2] = weight
            mst.graph_matrix[vertex2][vertex1] = weight

            # Yhdistetään kummatkin avaimet muihin
            heritage(parent, rank, n, m)

    return mst
    
 
if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 6, 0, 0, 5, 0], # 0
        [6, 0, 3, 3, 3, 0], # 1
        [0, 3, 0, 0, 6, 1], # 2
        [0, 3, 0, 0, 0, 5], # 3
        [5, 3, 6, 0, 0, 0], # 4
        [0, 0, 1, 5, 0, 0]  # 5    
    ]
    graph = Graph(matrix)
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)

    # Testi printti
    N = mst.vertex_count
    for i in range(N):
        for j in range(N):
            print(f"{mst.graph_matrix[i][j]:3d}", end="")
        print()
    print()

    mst.bf_print(0)     # 0 3 2 1 5 4