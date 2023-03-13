n = 5

def fatorialrecursivo(n):
    if n == 0:
        return 1
    x = n*fatorialrecursivo(n - 1)
    return x

print(fatorialrecursivo(n))