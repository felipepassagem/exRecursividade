#Escreva uma função recursiva que encontre o k-ésimo maior elemento em uma lista de números.

def encontraMaior(n, lista, index):
  if index == 0:
    return lista[index]
  if encontraMaior(n, lista, index - 1) > lista[index]:
    swap(index-1, index, lista)
    encontraMaior(1, lista, index)
    return lista[index]
  
  
def swap(maior, menor, lista):
  lista[maior], lista[menor] = lista[menor], lista[maior]
  return lista

lista = [3,2,1,8,6,3,5,10]

#print(swap(0, 2, lista))

print(encontraMaior(1, lista,7))
print(lista)