#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadas = {
    'jogador01': randint(1,6),
    'jogador02': randint(1,6),
    'jogador03': randint(1,6),
    'jogador04': randint(1,6)
}
rankink = dict()

print(jogadas)
rankink = sorted(jogadas.items(), key=itemgetter(1))

print(rankink)