# ìm ước chung lớn nhất
def InputData():
    a = int(input("Nhap so thu nhat: "))
    b = int(input("Nhap so thu hai: "))
    return a, b

def UCLN(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    a, b= InputData()
    max = UCLN(a, b)
    print("Ước chung lớn nhất là=%d "%max)

if __name__ == "__main__":
    main()
