M = []
n  = 10

def CreateArr(M, n):
  for i in range(n):
    M.append(int(input("Nhập phần tử thứ %d: "%(i+1))))
  
def ViewArr(M, n):
  for i in range(n):
    print("%d\t"%M[i], end = ' ')
  print()


def SumArr(M, n):
  s = 0
  for i in range(n):
    s += int(M[i])
  return s

def SumLe(M, n):
  for i in range(n):
    if int(M[i]) % 2 != 0:
      s += int(M[i])
  return s

def SortArr(M, n):
  for i in range(n):
    for j in range(n):
      if int(M[j]) > int(M[i]):
        temp = M[i]
        M[i] = M[j]
        M[j] = temp

def DeleteArr(M, n):
  for i in range(n):
    M[i] = M[i + 1]
  n = n - 1
  return n

def InsertArr(M, n, k, x):
  for i in range(n, k, -1):
    M[i] = M[i - 1]
  M[k] = x
  n = n + 1
  return n

def Input(x):
  try: 
    n = int(input("Nhập "+x+": "))
    if n <= 0:
      exit()
    return n
  except:
    print("Phai nhap so tu nhien")
    exit()

def main():
  n = Input("n");CreateArr(M, n);ViewArr(M, n)
  s = SumArr(M, n);print("Tong = ", s, "\n");SortArr(M, n);ViewArr(M, n)
  k = Input("k");m = DeleteArr(M, n, k);ViewArr(M, m)
  m = InsertArr(M, n, 2, 100);ViewArr(M, m)

if __name__ == "__main__":
  main()