n, m = (int(tmp) for tmp in input().split(" "))
INF = 999999
NIL = -1

matrizAdj = [[INF for col in range(n)] for row in range(n)]
for i in range (0, n):
  matrizAdj[i][i] = 0
for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  matrizAdj[i][j] = peso
for i in range (0, n):
  saida = ""
  for j in range (0, n):
    if matrizAdj[i][j] >= INF:
      saida += "INF "
    else:
      saida += "%d " % matrizAdj[i][j]

d = [np.copy(matrizAdj), np.copy(matrizAdj)]

tmp = [[NIL for col in range(n)] for row in range(n)]
for i in range (0, n):
  for j in range (0, n):
    if matrizAdj[i][j] < INF:
      tmp[i][j] = i

for i in range (0, n):
  tmp[i][i] = NIL
pi = [np.copy(tmp), np.copy(tmp)]

for k in range(1, n+1):
  for i in range(n):
    for j in range(n):
      d[k%2][i][j] = d[(k-1)%2][i][j]
      pi[k%2][i][j] = pi[(k-1)%2][i][j]
      if d[(k-1)%2][i][k-1] + d[(k-1)%2][k-1][j] < d[(k-1)%2][i][j]:
        d[k%2][i][j] = d[(k-1)%2][i][k-1] + d[(k-1)%2][k-1][j]
        pi[k%2][i][j] = pi[(k-1)%2][k-1][j]
 
print(d[k%2])
print(pi[k%2])