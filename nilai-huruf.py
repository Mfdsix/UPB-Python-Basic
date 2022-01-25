name = None
nim = None
mark = 0

def showWelcome():
    print("--------------- +++++ ---------------")
    print("            SELAMAT DATANG     ")
    print("--------------- +++++ ---------------")
    inputName()

def inputName():
    global name
    name = input("Silahkan Tulis Nama Anda: ")
    if name == None or name == "":
        print("Nama Tidak Boleh Kosong")
        inputName()
    else:
        inputNim()

def inputNim():
    global nim
    nim = input("Silahkan Tulis NIM Anda: ")
    if nim == None or nim == "":
        print("NIM Tidak Boleh Kosong")
        inputNim()
    else:
        inputMark()

def inputMark():
    global mark
    mark = input("Silahkan Tulis Nilai Anda (0-100): ")
    if mark == None or mark == "":
        print("Nilai Tidak Boleh Kosong")
        inputMark()
    elif not mark.isnumeric:
        print("Nilai Tidak Valid")
        inputMark()
    else:
        mark = int(mark)
        if mark < 0 or mark > 100:
            print("Nilai Harus Diantara 0 Sampai 100")
            inputMark()
        else:
            if mark >= 0 and mark < 50:
                printResult("E")
            elif mark >= 50 and mark < 60:
                printResult("D")
            elif mark >= 60 and mark < 70:
                printResult("C")
            elif mark >= 70 and mark < 80:
                printResult("B")
            elif mark >= 80 and mark <= 100:
                printResult("A")
            else: printResult("-")
                
def printResult(alphabetMark):
    print("--------------- +++++ ---------------")
    print("Nama :", name)
    print("NIM :", nim)
    print("Nilai :", str(mark) + " (" + alphabetMark + ")")
    print("--------------- +++++ ---------------")

    input("Tekan Enter Untuk Melanjutkan")
    showWelcome()

if __name__ == '__main__':
    try:
        showWelcome()
    except KeyboardInterrupt:
        print("Program Selesai")