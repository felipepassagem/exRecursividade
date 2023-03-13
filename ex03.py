
# def divisorcomumrec(n1, n2, div):
#     div = 2
#     maxdiv = 1
#     if n1 == 1 and n2 == 1:
#         return
#     if n1 % div == 0 and  n2 % div == 0:
#         maxdiv *= div
#     else:
        
        
      

#     else:
#         return divisorcomumrec()

# def teste(n, div):
#     dc = 1
#     if n == 1:
#       return 1
#     else:
#         if n % div == 0:
#             # dc *= div
#             return div * teste(n / div, div)
#         else:
#             div += 1
#             return  teste(n, div)
            
    
#print(teste(10, 2))

def divcomumrecursivo(n1, n2, div):
    if n1 == 1 and n2 == 1:
        return 1
    if n1 % div == 0 and n2 % div == 0:
        n1 /= div
        n2 /= div
        return div *  divcomumrecursivo(n1, n2, div)
    if n1 % div == 0:
        n1 /= div
        div += 1
        return divcomumrecursivo(n1, n2, div)
    elif n2 % div == 0:
        n2 /= div
        div += 1
        return divcomumrecursivo(n1, n2, div)
    else:
        div += 1
        return divcomumrecursivo(n1, n2, div)
    
print(divcomumrecursivo(18, 60, 2))
    

        


# def divisorcomum(n1, n2):
#     divisorcomum = 1
#     divisor = 2
#     while n1 != 1 or n2 != 1:
#         if n1 % divisor == 0 and n2 % divisor == 0:
#           divisorcomum *= divisor
#           #aux.append(divisor)
#           n1 /= divisor
#           n2 /= divisor
#         else:
#             if n1 % divisor == 0:
#                 n1 /= divisor
#             if n2 % divisor == 0:
#                 n2 /= divisor
#             divisor += 1
#     return divisorcomum

# print(divisorcomum(33,11))