#calcula a soma dos digitos do numero  inteiro passado

def calculasomadigitos(n, len,i):
    if len == 0:
        return int(n[0])
    return int(n[len]) + calculasomadigitos(n, len -1, i )

p1= "999"
plen = len(p1) -1

print(calculasomadigitos(p1, plen, 1))
