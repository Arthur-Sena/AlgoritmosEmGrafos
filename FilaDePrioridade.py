import numpy as np

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
  return min   #devolve indice de um vertice

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
  
n, k = (int(tmp) for tmp in input().split(" "))
tmp2 = list (int(tmp) for tmp in input().split(" "))
chave = np.array (tmp2)

# fila inicialmente vazia
Q = [0] * n
# leitura das operacoes
for i in range (k):
  op = input ()
  if (len(op) > 1):
    op, j = op.split(" ")
    j = int (j)
  if op == "I":
    insere (Q, j)
    print (Q)
  elif op == "M":
    print (minimo (Q, chave), chave[minimo (Q, chave)], Q)
  elif op == "E":
    chaveMinima = chave[minimo (Q, chave)]
    print (extraiMinimo (Q, chave), chaveMinima, Q)
  elif op == "V":
    print (vazio (Q), Q)
  elif op == "B":
    print (busca (Q, j), Q)