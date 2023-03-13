def mmcrec(n1,n2,div):
    if n1 == 1 and n2 ==1:
        return 1
    if n1 % div == 0 and n2 % div == 0:
        n1 /= div
        n2 /= div
        return div * mmcrec(n1,n2,div)
    if n1 % div == 0:
        n1 /= div
        return div * mmcrec(n1,n2,div)
    if n2 % div == 0:
        n2 /= div
        return div * mmcrec(n1, n2,div)
    div += 1
    return mmcrec(n1,n2,div)

print(mmcrec(60,120,2))