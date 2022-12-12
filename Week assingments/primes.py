def primes(N):
    primenumbers = []

    # Käydään läpi kaikki luvut välillä 2 ja N
    for i in range(2, N + 1):

        # Käydään läpi kaikki luvut välillä 2 ja i
        # Lähteet: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
        for j in range(2, i):
            # Jos i on jaollinen j:llä, niin luku ei ole alkuluku
            if i % j == 0:
                break
        else:
            primenumbers.append(i)
            
    return len(primenumbers)


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15