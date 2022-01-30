nama = input("Nama Lengkap: ")
nim = input("NIM: ")
nilai = input("Nilai (0-100): ")

nilaiAlpabet = "-"

nilai = int(nilai)
if nilai >= 0 and nilai < 50:
    nilaiAlpabet = "E"
elif nilai >= 50 and nilai < 60:
    nilaiAlpabet = "D"
elif nilai >= 60 and nilai < 70:
    nilaiAlpabet = "C"
elif nilai >= 70 and nilai < 80:
    nilaiAlpabet = "B"
elif nilai >= 80 and nilai <= 100:
    nilaiAlpabet = "A"

print("Nilai Alpabet: ", nilaiAlpabet)