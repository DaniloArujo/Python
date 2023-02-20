#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    num = int(input('Digite um valor entre 0 e 10: '))

    if num < 0 or num > 10:
        print('Numero inválido')

    else:
        print(f'O numero escolhido foi o {tupla[num]}')