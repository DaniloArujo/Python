#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

contador = 0

while True:
    escolha = input('Escolha Par ou Impar: ').lower()[0]
    if (escolha != 'p' and escolha != 'i'):
        print('jogada inválida')
        continue

    jogada = int(input('Digite um numero: '))
    jogadapc = random.randint(0,10)
    
    if escolha == 'p':
        if(jogada + jogadapc) % 2 == 0:
            print(f'você jogou {jogada} e o computador jogou {jogadapc}. Você ganhou!')
            contador += 1

        else:
            print(f'você jogou {jogada} e o computador jogou {jogadapc}. Você perdeu!')
            break

    else:
        if(jogada + jogadapc) % 2 == 0:
            print(f'você jogou {jogada} e o computador jogou {jogadapc}. Você perdeu!')
            break

        else:
            print(f'você jogou {jogada} e o computador jogou {jogadapc}. Você ganhou!')
            contador += 1
        
print('você não ganhou nenhuma!'if contador == 0  else f'Partidas ganhas: {contador}' )