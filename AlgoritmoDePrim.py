def vazio (Q):
  for i in range (len(Q)):
    if Q[i] == 1:
      return False
  return True

def insere (Q, i):
  Q[i] = 1

def minimo (Q, chave):
  for i in range (len(Q)):
    if Q[i] == 1:
      min = i
      break
  for i in range (len(Q)):
    if Q[i] == 1  and chave[i] < chave[min]:
      min = i
  return min 

def extraiMinimo (Q, chave):
  for i in range (len(Q)):
    if Q[i] == 1:
      min = i
      break
  for i in range (len(Q)):
    if Q[i] == 1  and chave[i] < chave[min]:
      min = i
  Q[min] = 0
  return min   

def busca (Q, v):
  return Q[v]

#Algoritmo de Prim
n, m, r = (int(tmp) for tmp in input().split(" "))
matrizAdj = [[0 for col in range(n)] for row in range(n)]

for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  matrizAdj[i][j] = peso

INF = 999999
NIL = -1
chave = [0] * n
pai = [0] * n
for i in range (0, n):
  chave[i] = INF
  pai[i] = NIL
chave[r] = 0
Q = [1] * n    # todos na fila de prioridade

while not vazio(Q):
  u = extraiMinimo (Q, chave)
  for v in range(n):
    weight = matrizAdj[u][v]
    if weight > 0:
      if busca(Q, v) and weight < chave[v]:
        chave[v] = weight
        pai[v] = u

print (chave)
print (pai)