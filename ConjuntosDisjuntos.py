def findSet (S, x):
  for i in range (len(S)):
    for j in S[i]:
      if j == x:
        return i

def makeSet (S, x):
  S.append([x])

def union (S, x, y):
  i = findSet (S, x)
  j = findSet (S, y)
  S[i] += S[j]
  S[j].clear()

S = []
makeSet(S, 0)
makeSet(S, 1)
union(S,0,1)

n = int (input ())
# inicialmente S eh vazio
S = []
# leitura das operacoes
for i in range (n):
  tmp = input().split(" ")
  op = tmp[0]
  arg1 = tmp[1]
  if len(tmp) > 2:
    arg2 = tmp[2]
  if op == "M":
    makeSet (S, arg1)
    print (S)
  elif op == "F":
    print (findSet (S, arg1), S)
  elif op == "U":
    union (S, arg1, arg2)
    print (S)
