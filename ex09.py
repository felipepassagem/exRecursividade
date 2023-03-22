# media da soma dos elementos da lista

def mediarec(lista, index, bool):
    if index == 0:
        return lista[0]
    if bool == False:
        return lista[index] + mediarec(lista, index - 1, False)
    else:
        return (lista[index] + mediarec(lista, index - 1, False)) / (index + 1)
    
lista = [2,4,6,12]
index = len(lista) - 1

print(mediarec(lista, index, True))