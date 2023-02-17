#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.


num = int(input('Quantos numeros você quer ver ? '))
loop = 2


t1 = 0
t2 = 1

print(f'{t1} {t2}', end=' ')

while loop < num:

    t3 = t1 + t2
    print(f'{t3}', end=' ')
    

    t1 = t2
    t2 = t3


    loop += 1