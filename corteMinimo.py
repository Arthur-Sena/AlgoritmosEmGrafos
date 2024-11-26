import copy

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

def aumentaFluxo (matrizAdj, fluxo, P):
  # calcula fluxo usando caminho aumentante
  for i, j, peso in P:
    if matrizAdj[i][j] > 0:
      fluxo[i][j] += capacidadeAumentante
    else:
      fluxo[i][j] -= capacidadeAumentante
  # calcula rede residual usando o fluxo atualizado
  matrizAdjResidual = [[0 for col in range(n)] for row in range(n)]
  for i in range (n):
    for j in range (n):
      matrizAdjResidual[i][j] = matrizAdj[i][j]
  for i in range (n):
    for j in range (n):
      if fluxo[i][j] > 0:
        matrizAdjResidual[j][i] = fluxo[i][j]
        matrizAdjResidual[i][j] = matrizAdj[i][j] - fluxo[i][j]
  return fluxo, matrizAdjResidual

fluxo = [[0 for col in range(n)] for row in range(n)]

# inicialmente a matriz de adjacencia da rede residual eh igual ao grafo de entrada
matrizAdjResidual = copy.deepcopy(matrizAdj)

# calcula caminho aumentante na rede residual
P, capacidadeAumentante = caminhoAumentante (matrizAdjResidual)

# enqto existe P, aumenta fluxo
while capacidadeAumentante > 0:
  fluxo, matrizAdjResidual = aumentaFluxo (matrizAdj, fluxo, P)
  P, capacidadeAumentante = caminhoAumentante (matrizAdjResidual)

print (fluxo)
print (matrizAdjResidual)

soma = 0
for i in range (n):
  soma += fluxo[i][t]
print (soma)

# alterado para corte minimo
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
  # marca vértices atingíveis a partir de s
  atingiveis = [0] * n
  # busca em largura
  while not vazio (Q):
    u = remove (Q)
    atingiveis[u] = 1
    for v, peso in adj[u]:
      if cor[v] == BRANCO:
        pi[v] = u
        cor[v] = CINZA
        insere (Q, v)
    cor[u] = PRETO
  return pi, atingiveis

pi, atingiveis = bfs (matrizAdjResidual, n, s)

matrizCorte = [[0 for col in range(n)] for row in range(n)]
for i in range(n):
  for j in range(n):
    if matrizAdj[i][j] > 0 and atingiveis[i] != atingiveis[j]:
      matrizCorte[i][j] = 1
print (matrizCorte)