def split(T):
    value = 0
    divide = 0
    for i in range(len(T)):
        value = value + T[i]
    print(value)
    for i in range(len(T)):
        divide = divide + T[i]

if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    #print(split([5,4,3,2,1])) # 0
    #print(split([2,1,2,5,7,6,9])) # 3
    #print(split([1,2,3,1])) # 0