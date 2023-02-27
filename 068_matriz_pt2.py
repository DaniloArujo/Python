#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B)A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.


matriz = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(3):
    for y in range(3):
        matriz[x][y] = int(input('Digite um valor: '))

print(matriz)