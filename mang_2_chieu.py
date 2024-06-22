A = []; B = []; C = []; D = []
m = 2; n = 2

def CreateMatrix(A, m, n, c):
  for i in range(m):
    A.append([])
    for j in range(n):
      x = int(input("%c[%d][%d]: "%(c, i+1, j+1)))
      A[i].append(x)

def ViewMatrix(A, m, n):
  for i in range(m):
    for j in range(n):
      print("%d"%A[i][j], end = ' ')
    print()

def SumMatrix (A, B, m, n):
  C = []
  for i in range(m):
    C.append([])
    for j in range(n):
      C[i].append(A[i][j] + B[i][j])
  return C


def MulMatrix(A, B, m, n):
  D =[]
  for i in range(m):
    D.append([])
    for j in range(n):
      x = 0
      for k in range(m):
        x += A[i][k] * B[k][j]
      D[i].append(x)
  return D

def main():
  print("Tao ma tran A: ", end = '\n'); CreateMatrix(A, m, n, 'A')
  print("Xem ma tran A: ", end = '\n'); ViewMatrix(A, m, n)
  print("Tao ma tra B: ", end = '\n'); CreateMatrix(B, m, n, 'B')
  print("Xem ma tran B: ", end = '\n'); ViewMatrix(B, m, n)
  C = MulMatrix(A, B, m, n)
  print("Xem ma tran C: ", end = '\n'); ViewMatrix(C, m, n)
if __name__ == "__main__":
  main()