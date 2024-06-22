def InputData():
  n = int(input("Nhập n: "))
  return n

def GiaiThua(n):
  s = 1
  for i in range(1, n+1):
    s *= i
  return s

def main():
  n = InputData()
  s = GiaiThua(n)
  print("%d"%n, "! = %d"%s)

if __name__ == "__main__":
  main()