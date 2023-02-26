#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista_pessoas = list()
tamanho_lista = 0

while True:
    pessoa = list()

    nome = input('digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa: '))
    
    pessoa.append(nome)
    pessoa.append(peso)

    lista_pessoas.append(pessoa)
    
    parar = input('Deseja continuar?(n)')
    if parar in "Nn":
        break
print(lista_pessoas)