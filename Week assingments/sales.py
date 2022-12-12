def sales(cars, customers) -> int:
    sales = 0
    #Laitetaan listat järjestykseen pienimmästä suurimpaan
    cars.sort()
    customers.sort()
    #Käydään läpi asiakkaat ja autot
    for i in customers:
        for j in cars:
            #Jos auto on pienempi tai yhtä suuri kuin asiakas, myydään auto
            if j <= i:
                sales = sales + 1
                #Poistetaan auto listasta jotta sitä ei myydä uudelleen
                cars.remove(j)
                break

    return sales

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))          # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5  