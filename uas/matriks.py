matrik1 = [
    [ 1, 2, 5 ],
    [ 3, 4, 10 ],
    [ 5, 12, 8 ]
]
matrik2 = [
    [ 10, 20, 5 ],
    [ 30, 40, 4 ],
    [ 8, 17, 19 ],
]

hasil = []
print("----------------------- MENJUMLAHKAN MATRIKS -----------------------")
for i in range(len(matrik1)):
    hasil.insert(i, [])
    for ii in range(len(matrik1[i])):
        value1 = matrik1[i][ii]
        value2 = matrik2[i][ii]

        hasil[i].insert(ii, value1 + value2)

print("---- Matriks 1")
for i in range(len(matrik1)):
    print(matrik1[i])

print("---- Matriks 2")
for i in range(len(matrik2)):
    print(matrik2[i])

print("---- Hasil")
for i in range(len(hasil)):
    print(hasil[i])