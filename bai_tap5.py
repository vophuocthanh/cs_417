# Tìm số lớn nhất trong 3 số
def InputData():
  a = int(input("Nhập số thứ nhất: "))
  b = int(input("Nhập số thứ hai: "))
  c = int(input("Nhập số thứ ba: "))
  return a, b, c

def Max(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c
  
def main():
  a, b, c = InputData()
  max = Max(a, b, c)
  print("Số lớn nhất trong 3 số là: ", max)

if __name__ == "__main__":
  main()
