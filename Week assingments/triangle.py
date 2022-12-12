def triangle(a, b, c):
    # Sivut muodostavat kolmion jos kaksi lyhyintä sivua ovat pidempiä kuin pisin sivu
    # Tarkistetaan pisin sivu
    if a <= c and b <= c:
        # Tarkistetaan pitääkö kolmion ehto paikkansa
        if a + b > c:
            return True
        else:
            return False
    elif a <= b and c <= b:
        if a + c > b:
            return True
        else:
            return False
    elif b <= a and c <= a:
        if b + c > a:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    print(triangle(1, 5, 5))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True