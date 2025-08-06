import numpy as np

# Tworzymy tablicę z danymi pogodowymi
# Każdy wiersz to jeden dzień pomiarów
# Kolumny reprezentują: temperatura, ciśnienie, wilgotność
pomiary = np.array([
    [25, 1013, 60],    # Dzień 1
    [24, 1015, 65],    # Dzień 2
    [26, 1010, 55],    # Dzień 3
    [23, 1012, 70],    # Dzień 4
    [22, 1014, 75],    # Dzień 5
    [27, 1011, 58]     # Dzień 6
])

# Dzielimy dane na 3 osobne kolumny używając array_split
dane_podzielone = np.array_split(pomiary, 3, axis=1)

# Wyświetlamy wynik
for i, kolumna in enumerate(dane_podzielone):
    if i == 0:
        print("Temperatura dla kolejnych dni:")
        for temp in kolumna:
            print(f"{temp[0]} st c")
    elif i == 1:
        print("\nCiśnienie dla kolejnych dni:")
        print(kolumna)
    else:
        print("\nWilgotność dla kolejnych dni:")
        print(kolumna)
def dodaj_jednostke(x):
    return f"{x} hPa"

formatuj = np.vectorize(dodaj_jednostke)
print("\nAlternatywnie: ")
print("Ciśnienie: ")
print(formatuj(dane_podzielone[1]))