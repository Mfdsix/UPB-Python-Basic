start = 1
end = 100

def cekPrima(number):
    if number == 1:
        return False

    for i in range(2, number-1):
        if number % i == 0:
            return False
    
    return True

print("----------------------- MENCARI BILANGAN PRIMA -----------------------")
print("--- Range ", start, "sampai", end)
for number in range(start, end):
    print(number, "PRIMA" if cekPrima(number) else "x")