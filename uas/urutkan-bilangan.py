angka = [34, 38, 27,29]

print("----------------------- MENGURUTKAN BILANGAN -----------------------")
print("--- Urutan Awal")
print(", ".join(map(str,angka)))
angka.sort()
print("--- Hasil")
print(", ".join(map(str,angka)))