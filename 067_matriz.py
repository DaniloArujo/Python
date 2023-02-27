#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(3):
    for y in range(3):
        matriz [x][y] = int(input(f'Digite um valor para a posição [{x}][{y}]: '))

for elem in matriz:
    print(elem)