def subsets(n: int) -> list:
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        remainlst_combo = subsets(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
           
    return l


if __name__ == "__main__":
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    #print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]

    #S = subsets(10)
    #print(S[95])    # [6, 7]
    #print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    #rint(S[826])   # [1, 2, 4, 5, 6, 9, 10]