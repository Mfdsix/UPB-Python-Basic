numberStart = 2
numberEnd = 100
divider = 3

def showWelcome():
    print("----------------------- +++++ -----------------------")
    print("Mencari Bilangan Ganjil Habis Dibagi " + str(divider) + " Diantara " + str(numberStart) + "-" + str(numberEnd))
    print("----------------------- +++++ -----------------------")
    mainProcess()

def checkOdd(number):
    return number % 2 != 0

def checkDivided(number):
    return number % divider == 0

def mainProcess():
    for i in range(numberStart, numberEnd):
        print(i) if checkOdd(i) and checkDivided(i) else False
    print("----------------------- +++++ -----------------------")

if __name__ == '__main__':
    try:
        showWelcome()
    except KeyboardInterrupt:
        print("Program Selesai")