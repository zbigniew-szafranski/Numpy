# import numpy as np
#
# # Tworzymy tablicę z danymi pogodowymi
# # Każdy wiersz to jeden dzień pomiarów
# # Kolumny reprezentują: temperatura, ciśnienie, wilgotność
# pomiary = np.array([
#     [25, 1013, 60],    # Dzień 1
#     [24, 1015, 65],    # Dzień 2
#     [26, 1010, 55],    # Dzień 3
#     [23, 1012, 70],    # Dzień 4
#     [22, 1014, 75],    # Dzień 5
#     [27, 1011, 58]     # Dzień 6
# ])
#
# # Dzielimy dane na 3 osobne kolumny używając array_split
# dane_podzielone = np.array_split(pomiary, 3, axis=1)
#
# # Wyświetlamy wynik
# for i, kolumna in enumerate(dane_podzielone):
#     if i == 0:
#         print("Temperatura dla kolejnych dni:")
#         for temp in kolumna:
#             print(f"{temp[0]} st c")
#     elif i == 1:
#         print("\nCiśnienie dla kolejnych dni:")
#         print(kolumna)
#     else:
#         print("\nWilgotność dla kolejnych dni:")
#         print(kolumna)
# def dodaj_jednostke(x):
#     return f"{x} hPa"
#
# formatuj = np.vectorize(dodaj_jednostke)
# print("\nAlternatywnie: ")
# print("Ciśnienie: ")
# print(formatuj(dane_podzielone[1]))
from statistics import median

# import numpy as np
# from numpy import random
# import matplotlib.pyplot as plt  # do wizualizacji wyników
#
# # Symulacja rzutów monetą
# # n=10 (liczba prób/rzutów monetą)
# # p=0.5 (prawdopodobieństwo sukcesu - wypadnięcia orła)
# # size=10 (ile razy przeprowadzamy eksperyment)
#
# rzuty = random.binomial(n=10, p=0.5, size=10)
# print("Wyniki 10 eksperymentów (liczba orłów w 10 rzutach):")
# print(rzuty)
#
# # Większa liczba eksperymentów dla lepszej wizualizacji
# duza_proba = random.binomial(n=10, p=0.5, size=1000)
#
# print("\nStatystyki dla 1000 eksperymentów:")
# print(f"Średnia liczba orłów: {np.mean(duza_proba):.2f}")
# print(f"Odchylenie standardowe: {np.std(duza_proba):.2f}")
#
# # Histogram wyników
# plt.figure(figsize=(10, 6))
# plt.hist(duza_proba, bins=11, density=True, alpha=0.7, color='blue')
# plt.title('Rozkład liczby orłów w 10 rzutach monetą')
# plt.xlabel('Liczba orłów')
# plt.ylabel('Częstość')
# plt.grid(True, alpha=0.3)
# plt.show()

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from seaborn.external.docscrape import header

# temperatury = np.array([
#     [25, 28, 30, 27, 26, 24, 23],  # Miasto A
#     [20, 22, 24, 23, 21, 19, 18],  # Miasto B
#     [30, 32, 35, 33, 31, 29, 28]   # Miasto C
# ])
#
# srednie_temp = temperatury.mean(axis=1)
# miasta = ["Opole", "Wrocław", "Gdynia"]
#
# for i in range(len(miasta)):
#     print(f"{miasta[i]} średnia temp: {int(srednie_temp[i])}")

# text = np.loadtxt('dane1.txt')
# mediana = np.median(text)
#
# print(len(text))
#
# print(f"Średnia {np.mean(text):.2f}")
# print(f"Mediana {np.median(text):.2f}")
# print(f"Odchylenie {np.std(text):.2f}")
#
# text2 = text[text>50]
# print(f"Liczb większych od 50 jest: {len(text2)}")
#
# srednia_75 = text[text>75].mean()
# print(f"Średnia arytmetyczna liczb większych niż 75 wynosi: {srednia_75:.2f}")
#
# plt.figure(figsize=(10,6))
# plt.hist(text, bins=30, color='skyblue', edgecolor='black')
# plt.title('Rozkład liczb z dane1.txt')
# plt.xlabel('Wartość liczby')
# plt.ylabel('Częstotliwość występowania')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.show()
#
# plt.figure(figsize=(8,6))
# plt.boxplot(text, vert=True, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
# plt.title('Wykres pudełkowy liczb z dane1.txt')
# plt.ylabel('Wartość liczby')
# plt.yticks([])
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.text(1.05, mediana, f'Mediana: {mediana:.2f}', va='center', ha='left', color='red', fontsize=10)
# plt.show()

# arr = np.array([[10, 60, 30, 80],
#           [70, 20, 90, 40],
#           [55, 15, 65, 25],
#           [12, 88, 42, 72],
#           [95,  5, 28, 68]])
#
# miasta = ["Kiełczów", "Kłodzko", "Wieluń", "Domaszków"]
# produkty = ["Mąka", "Chleb", "Woda", "Masło", "Zioła"]
#
# processed_arr = np.where(arr>50, arr, 0)
#
# max_sales_per_city = np.max(processed_arr, axis=0)
#
# best_products_above_50 = []
# for col_idx, max_val in enumerate(max_sales_per_city):
#     if max_val>0:
#         row_indices = np.where(processed_arr[:, col_idx] == max_val)[0]
#         if len(row_indices)>0:
#             best_products_above_50.append(produkty[row_indices[0]])
#         else:
#             best_products_above_50.append("Błąd")
#
#     else:
#         best_products_above_50.append("Brak sprzedaży > 50")
#
# df_original = pd.DataFrame(arr, columns=miasta, index=produkty)
# df_filtered = pd.DataFrame(processed_arr, columns=miasta, index=produkty)
#
# df_results = pd.DataFrame({
#     "Miasto": miasta,
#     "Maksymalna Sprzedaż > 50": max_sales_per_city,
#     "Produkt z największą sprzedażą (>50)": best_products_above_50
# })
# output_filename = "sprzedaże.xlsx"
# sheet_name = "Raport Sprzedaży"
#
# with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
#     df_original.to_excel(writer, sheet_name=sheet_name, startrow=0, index=True, header=True)
#
#     startrow_filtered = len(df_original) + 3
#     df_filtered.to_excel(writer, sheet_name=sheet_name, startrow=startrow_filtered, index=True, header=True)
#
#     startrow_results = startrow_filtered + len(df_filtered) +3
#     df_results.to_excel(writer, sheet_name=sheet_name, startrow=startrow_results, index=False, header=True)
#
# print(f"Dane zostały zapisane do pliku '{output_filename}' w arkuszu '{sheet_name}'")

# data = np.loadtxt('dane.txt')
# num_columns = 7
# num_elements_to_slice = (len(data)//num_columns) * num_columns
# sliced = data[:num_elements_to_slice]
# data_sliced = sliced.reshape(-1, num_columns)
# mean_per_day = np.mean(data_sliced, axis=0)
# week_sum = np.sum(data_sliced, axis=1)
# week_max_index = np.argmax(week_sum)
#
# print("Średnie wartości dla każdego dnia tygodnia:", mean_per_day)
#
# day_with_highest_avg = np.argmax(mean_per_day)
# print(f"Dzień tygodnia z najwyższą średnią wartością to dzień numer: {day_with_highest_avg} (indeks 0-6")
# print(f"Najwyższa średnia wartość wynosi:{mean_per_day[day_with_highest_avg]:.2f}")
#
# print(f"\nTydzień, w którym suma pomiarów była najwyższa to tydzień numer: {week_max_index}")
# print(f"Suma pomiarów w tym tygodniu wynosi: {week_sum[week_max_index]:.2f}")


# over_50 = data[data>50]
#
# print("Średnia:",  np.mean(over_50))
# print("Mediana", np.median(over_50))
# print("Odchylenie:", np.std(over_50))
file_name_1 = 'dane.txt'
file_name_2 = 'dane1.txt'
ingredients_1 = np.loadtxt(file_name_1)
ingredients_2 = np.loadtxt(file_name_2)

def display_ingredeints(data, name):
    print("Smaki:")
    print(f"Przeciętny smak {name}: {np.mean(data):.2f}")
    print(f"Równe połowy {name} : {np.median(data):.2f}")
    print(f"Jak bardzo różnią się smaki {name}: {np.std(data):.2f}")
    print(f"Najmniej smakowity {name}: {np.min(data):.2f}")
    print(f"Najbardziej smakowity {name}: {np.max(data):.2f}")
    print('------------------------------------------')

def display_spec(data, name):
    avg_taste = np.mean(data)
    threshold = 2 * avg_taste

    premium_ingredients = data[data >= threshold]

    count_premium = len(premium_ingredients)

    print(f"\n--- Składniki premium w {name} ---")
    print(f"Średni smak partii: {avg_taste:.2f}")
    print(f"Próg smaku dla składników premium (2 x średnia): {threshold:.2f}")
    print(f"Liczba składników premium w {name}: {count_premium}")

display_ingredeints(ingredients_1, file_name_1)
display_ingredeints(ingredients_2, file_name_2)
display_spec(ingredients_2, file_name_2)