# Viết chương trình bậc 2
import math
def InputData ():
  print("Nhập các hệ số của phương trình bậc 2: ")
  a = float(input("Nhập a: "))
  b = float(input("Nhập b: "))
  c = float(input("Nhập c: "))
  return a, b, c

def SolveEqual(a, b, c):
  if a == 0 and b == 0 and c == 0:
    print("Phuong trinh co vo so nghiem")
  elif a == 0 and b == 0 and c != 0:
    print("Phuong trinh vo nghiem")
  elif a == 0 and b != 0:
    x = -c / b
    print("ptb1 x=", str(x))
  else:
    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0 :
      x1 = (-b + math.sqrt(delta)) / (2 * a)
      x2 = (-b - math.sqrt(delta)) / (2 * a)
      print("Nghiem phan biet: \n")
      print("x=%.3lf="%x1, "x2=%.3lf"%x2)
    elif delta == 0:
      x0 = -b / (2 * a)
      print("phuong trinh co nghiem kep: \n")
      print("x0 = %.2f"%(x0))
    else:
      print("Vo nghiem thuc.")

def main():
  a, b, c = InputData()
  SolveEqual(a, b, c)
if __name__ == "__main__":
  main()