# Obtém as **listas de adjacência** (da matriz de adj.).
def calculaListasAdjacencia (matrizAdj):
  # cria listas de adjacencias
  adj = [[] for _ in range(n)]
  for i in range (n):
    for j in range (n):
      peso = matrizAdj[i][j]
      if peso > 0:
        # insere vizinho j
        adj[i].append ([j, peso])
  return adj

# FILA
# Assume que Q eh uma lista
def insere (Q, x):
  Q.append (x)

# Assume que Q nao eh vazio
def remove (Q):
  return Q.pop (0)

def vazio (Q):
  if len (Q) == 0:
    return True
  else:
    return False

# BFS: busca em largura para encontrar caminhos aumentantes na rede residual
def bfs (matrizAdj, n, s):
  adj = calculaListasAdjacencia (matrizAdj)
  # inicializacao
  NIL = -1
  BRANCO = 1
  CINZA = 2
  PRETO = 3
  pi = [NIL] * n
  cor = [0] * n
  for v in range (0, n):
    cor[v] = BRANCO
  cor[s] = CINZA
  Q = []
  insere (Q, s)
  # busca em largura
  while not vazio (Q):
    u = remove (Q)
    for v, peso in adj[u]:
      if cor[v] == BRANCO:
        pi[v] = u
        cor[v] = CINZA
        insere (Q, v)
    cor[u] = PRETO
  return pi

def caminhoAumentante (matrizAdj):
  pi = bfs (matrizAdj, n, s)
  #print (pi)
  # caminho (aumentante) de s a t
  NIL = -1
  INF = 999999
  capacidadeAumentante = INF
  j = t
  P = []
  while pi[j] != NIL:
    i = pi[j]
    peso = matrizAdj[i][j]
    P.insert(0, [i, j, peso])    # insere no comeco da lista
    if peso < capacidadeAumentante:
      capacidadeAumentante = matrizAdj[i][j]
    j = i
  if capacidadeAumentante == INF:
    capacidadeAumentante = 0
  return P, capacidadeAumentante

# leitura dos dados de entrada do EP
n, m, s, t = (int(tmp) for tmp in input().split(" "))
# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]
for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  # marca arco com o peso
  matrizAdj[i][j] = peso

P, capacidadeAumentante = caminhoAumentante (matrizAdj)
print (P)
print (capacidadeAumentante)


