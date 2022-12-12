#Lähteet:
#https://www.geeksforgeeks.org/python-program-for-quicksort/
#https://www.programiz.com/dsa/quick-sort

def qsort(A, i, j):
    if i < j:
        p = partition(A, i, j)
        #Kutsutaan rekursiivisesti pivotin vasemmalta
        qsort(A, i, p - 1)
        #Kutsutaan rekursiivisesti pivotin oikealta
        qsort(A, p + 1, j)

def partition(A, i, j):
    #Valitaan pivot arrayn lopusta
    pivot = A[j]
    #Väliaikais muuttuja arrayn alusta
    k = i
    #Käydään array läpi
    for l in range(i, j):
        #Vertaillaan jokaista arrayn arvoa pivotin kanssa
        #Jos läpikäytävä arvo on pienempi kuin pivotin arvo
        if A[l] <= pivot:
            #Vaihdetaan väliaikaisen muuttujan arvo läpikäytävän arvon kanssa
            A[k], A[l] = A[l], A[k]
            #Kasvatetaan väliaikaisen muuttujan arvoa
            k += 1
    #Vaihdetaan väliaikaisen muuttujan arvo pivotin kanssa
    A[k], A[j] = A[j], A[k]
    return k
    
  
if __name__ == "__main__":
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]