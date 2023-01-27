#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite a frase: ').strip().lower()

print(f'Ocorrencia A: {frase.count("a")}')

print(f'Primeira ocorrência: {frase.find("a")}')
print(f'Ultima ocorrência: {frase.rfind("a")}')
