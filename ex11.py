#soma de martiz n-dmensional

matriz = [[2,3], [1,1,1,1,1]]

def soma(matriz):
  contador = 0
  for lista in matriz:
      for el in lista:
          contador += el
  return contador


#soma lista
def somarecteste(n, l, matriz):
   if l == 0:
      return matriz[n][l]
   x = somarec(n, l -1, matriz)
   return x + matriz[n][l]

#funcao que deu certo
def somarec(n,l,matriz):
   if l == 0 and n == 0:
      return matriz[n][l]
   if l == 0 and n != 0:
      #n -= 1
      return somarec(n - 1, len(matriz[n - 1]) -1 , matriz) + matriz[n][l]
   if l != 0 and n == 0:
      return somarec(n, l -1, matriz) + matriz[n][l]
   if l != 0 and n != 0:
      return somarec(n, l-1, matriz) + matriz[n][l]
   
print(somarec(1, len(matriz[1])-1, matriz))


   

