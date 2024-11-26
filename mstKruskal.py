import numpy as np
n, m = (int(tmp) for tmp in input().split(" "))
matrizAdj = [[0 for col in range(n)] for row in range(n)]
for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  matrizAdj[i][j] = peso

arestas = []
for i in range (n):
  for j in range (i, n):
    if matrizAdj[i][j] > 0:
      peso = matrizAdj[i][j]
      arestas.append ([i,j,peso])

# inicializacao
T = []   # arvore geradora inicialmente vazia
S = []
for i in range (0, n):
  makeSet(S, i)

tmp = np.array(arestas)
ordenado = tmp[tmp[:, 2].argsort()]
for u,v,peso in ordenado:
  if findSet (S, u) != findSet (S, v):
    union (S, u, v)
    T.append ([u,v,peso])
print(T)

# custo total MST
tmp = np.array(T)
soma = tmp.sum(axis=0)
#soma dos pesos de T
# print (soma[2])