def maiorrec(lista, i):
    if i == 0:
      return lista[i]
    if lista[i] > maiorrec(lista, i - 1):
       x = lista[i]
    else:
       x = maiorrec(lista, i - 1)
    return x
    
    

lista = [4,7,2, 8 ,1]
i = len(lista) - 1

print(maiorrec(lista, i))