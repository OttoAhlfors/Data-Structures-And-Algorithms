#Lähteet:
#Kurssi materiaali: https://moodle.lut.fi/mod/page/view.php?id=698519

def jumps(n, a, b):
    #Toteutetaan rekursiivinen funktio
    if n == 0:
        # Hyppyjen määrä on funktion palauttamien ykösten määrä
        # Jos hyppy onnistuu, palautetaan 1
        return 1
    if n < 0:
        # Jos n on negatiivinen, ei viimeisintä hyppyä voida tehdä
        return 0
    # Vähennetään n:stä a ja b
    # näin saadaan suoritettua kumpikin mahdollinen hyppy
    return jumps(n - a, a, b) + jumps(n - b, a, b)

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937 