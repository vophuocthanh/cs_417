import math
def InputData ():
  a = float(input("Nhập a: "))
  b = float(input("Nhập b: "))
  return a, b

def SolveEqual(a, b):
  if a == 0:
    if b == 0:
      print("Phuong trinh co vo so nghiem")
    else:
      print("Phuong trinh vo nghiem")
  else:
    x = -b / a
    print("Nghiem x=%.3lf"%x, end = "\n")

def main():
  a,b = InputData()
  SolveEqual(a, b)
if __name__ == "__main__":
  main()

# def trong python dùng để đin nghĩa 1 hàm