def menorrec(lista, i):
    if i == 0:
      return lista[i]
    if lista[i] < menorrec(lista, i - 1):
       x = lista[i]
    else:
       x = menorrec(lista, i - 1)
    return x
    
    

lista = [4,7,2, 8,0 ,1]
i = len(lista) - 1

print(menorrec(lista, i))