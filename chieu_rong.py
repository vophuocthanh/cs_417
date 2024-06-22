G = []
def Init(path,G):
     f = open(path)
     n = int(f.readline(),base = 10)
     for i in range(n + 1):
          G.append([])
          for j in range(n + 1):
               G[i].append(0)
     while True:
          string = f.readline()
          if not string:
               break
          string = string.replace('\t','')
          k = string.index(' ')
          str = string[0:k]
          i = int(str,base = 10)
          m = string.index(' ', k+1,-1)
          str = string[k+1:m]
          j = int(str, base = 10)
          str = string[m + 1:len(string)]
          x = int(str, base = 10)
          G[i][j] = G[j][i] = x
     f.close()
     return n
def ViewMatrix(G,n):
     for i in range(1, n + 1):
          for j in range(1,n + 1):
               print("%d" % G[i][j], end = '')
          print()
def BFS(u, n):
     Q = []; C = []
     for j in range(n + 1):
          Q.append(0)
          C.append(0)
     frist = 1;last = 1;Q[last] = u; C[u] = 1
     while frist <= last:
          u = Q[frist]; frist = frist +1
          print("%d" %u, end = '\t')
          for v in range(1, n +1):
               if G[u][v] != 0 and C[v] == 0:
                    last = last +1
                    Q[last] = v
                    C[v] = 1
def main():
     n = Init("Graph2.inp", G)
     print("Xem ma tran G:", end = '\n')
     ViewMatrix(G,n)
     u = 3; BFS(u,n)
if __name__=="__main__":
     main()