# leitura dos dados de entrada do EP
n, m, s = (int(tmp) for tmp in input().split(" "))
# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]
for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  # marca arco com o peso
  matrizAdj[i][j] = peso

# inicializacao
INF = 999999
NIL = -1
d = [0] * n
pi = [0] * n
for i in range (0, n):
  d[i] = INF
  pi[i] = NIL
d[s] = 0
Q = [1] * n    # todos na fila de prioridade

while not vazio(Q):
  u = extraiMinimo (Q, d)
  for v in range(n):
    weight = matrizAdj[u][v]
    if weight > 0:
      # Relax (u,v,w)
      if d[u] + weight < d[v]:
        d[v] = d[u] + weight
        pi[v] = u

print (d)
print (pi)