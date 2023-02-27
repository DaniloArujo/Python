#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista_pessoas = list()
temp = list()
maior = menor = 0


while True:
    
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista_pessoas) == 0:
        menor = maior = temp[1]
    
    else:
        if temp[1] < menor:
            menor = temp[1]

        if temp[1] > maior:
            maior = temp[1]
    lista_pessoas.append(temp[:])
    temp.clear()
    
    parar = input('Deseja continuar?(n)')
    if parar in "Nn":
        break


print('-='*30)
print(f'voce cadastrou {len(lista_pessoas)} pessoas')
print(lista_pessoas)

for pessoa in lista_pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa} tem um dos menores pesos: {pessoa[1]}')

for pessoa in lista_pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa} tem um dos menores pesos {pessoa[1]}')