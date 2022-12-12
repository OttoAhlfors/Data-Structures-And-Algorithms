def salesman(city_map):
    path = [0]  * (len(city_map) + 1)
    found = [False] * len(city_map)
    start = 0
    length = 0
    minlenght = 999999
    for i in range(len(city_map)):
        for j in range(len(city_map)):
            print(i, j, city_map[i][j])
            if found[j] == False:
                print("lisätään", i, j, city_map[i][j])
                length = length + city_map[i][j]
                path[j] = j
                found[j] = True
                print("minlenght", minlenght)
            if False not in found:
                if length < minlenght:
                    minlenght = length
                break
        if False not in found:
                print("takaisin alkupisteeseen", city_map[j][start])
                break
    return path
    
    

if __name__ == "__main__":
    
    cost = 0

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45