angka = [34, 38, 27,29]
n = len(angka)

print("----------------------- MENGURUTKAN BILANGAN -----------------------")
print("--- Urutan Awal")
print(", ".join(map(str,angka)))
for i in range(n):
    for j in range(0, n-i-1):
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]

print("--- Hasil")
print(", ".join(map(str,angka)))