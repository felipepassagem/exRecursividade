# numeor de ocorrencias em uma lista de inteiros

# def calcularec(lista, n, index, bool):
#     if index == 0:
#         if lista[index] == n:
#             return n
#         else:
#             return 0
#     if bool == False:
#       if lista[index] == n:
#           return n + calcularec(lista, n, index -1,False)
#       else:
#           return calcularec(lista, n, index -1,False)
#     else:
#         if lista[index] == n:
#           return (n + calcularec(lista, n, index -1,False)) / n
#         else:
#           return calcularec(lista, n, index -1,False) / n

def calcularec2(lista, index, n):
    if index == 0:
        if lista[index] == n:
          return 1
        else:
           return 0
    if lista[index] == n:
       return 1 + calcularec2(lista, index - 1, n)
    return calcularec2(lista, index - 1, n)
        
    
lista = [2,5,2,7,2,9]
index = len(lista) - 1

#print(calcularec(lista, 7, index))
print(calcularec2(lista, index, 9))