def exporec(base, exp):
    if exp == 1:
      return base
    return base * exporec(base, exp -1)

print(exporec(3,8))