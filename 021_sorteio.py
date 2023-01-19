#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


import random

aluno1 = input('Digite o nome do aluno 01: ')
aluno2 = input('Digite o nome do aluno 02: ')
aluno3 = input('Digite o nome do aluno 03: ')
aluno4 = input('Digite o nome do aluno 04: ')

listaalunos = [aluno1,aluno2,aluno3,aluno4]


print(f'O aluno escolhido foi: {random.choice(listaalunos)}')

#random.random() = aleatório entre 0 e 1
#random.choice = para uma lista
#randint(1,10) = aleatório entre 1 e 10


print('**************************************************')

listaalunos = random.sample(listaalunos,k=2)
#O comando Sample embaralha e decide a quantidade de itens sorteados

print(f'A ordem de apresentação é a segunte: ')
print(listaalunos)