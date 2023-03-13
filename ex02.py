# fibo(n-1) + fibo(n -2)
n = 10

def fiborecursivo(n):
    # Se n for um indice inicial da sequencia
    if n <= 1:
        return n
    x = fiborecursivo(n - 1) + fiborecursivo(n - 2)  # Soma os dois numeros anteriores da sequencia
    return x



for i in range(n):
    print(fiborecursivo(i))
