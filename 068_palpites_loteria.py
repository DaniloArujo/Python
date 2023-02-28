#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random

palpites = list()
temp = list()

rodadas = int(input('Qualtos palpites você quer?: '))

for x in range(rodadas):

    for y in range(6):
        while True :
            numero = random.randint(1,60)
            if numero  not in temp:
                temp.append(numero)
                break

    palpites.append(temp[:])
    temp.clear()

for element in palpites:
    print(sorted(element))