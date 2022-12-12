def sums(items):
    ansvers = []
    x = 0
    for i in items: 
        tempSum = 0
        if i not in ansvers:
            ansvers.append(i)
        #print("location:", x, "key:", items[x])
        if 1 != 0:
            temp = items[x] + items[x - 1]
            if temp not in ansvers:
                ansvers.append(temp)
        x += 1
        for j in ansvers:
            tempSum = tempSum + j
            print("tempSum:", tempSum)
            if tempSum not in ansvers:
                ansvers.append(tempSum)
        
    #print("sums:", ansvers)
    return len(ansvers)

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    #print(sums([2, 2, 3]))                  # 5
    #print(sums([1, 3, 5, 1, 3, 5]))         # 18
    #print(sums([1, 15, 5, 23, 100, 55, 2])) # 121