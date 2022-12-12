def pairs(s):
    dist = 0
    for i in range(len(s)):
        if s[i] == "1":
            break
    for x in range(i, len(s)):
        if s[x] == "1":
            dist += x - i
    return dist


if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    #print(pairs("100100111001")) # 71