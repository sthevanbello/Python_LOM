numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_2 = {2, 3, 6, 8, 10, 12, 13, 15, 18}
print(numeros)
print(numeros_2)

# numeros.add(5)
# numeros.add(11)
# numeros.add(0)
# numeros.add(14)

set3 = numeros | numeros_2
set4 = numeros & numeros_2
set5 = numeros - numeros_2
set6 = numeros_2 - numeros
set7 = numeros ^ numeros_2
# numeros.update(numeros_2)

print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
