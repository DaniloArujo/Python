#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um valor: '))

if(numero > 9999 or numero < 0):
    print('Numero inválido')
else:
    if(numero == 0):
        print(f'O numero 0000 tem: ')
        print('0 unidades')
        print('0 dezenas')
        print('0 centenas')
        print('0 milhar')

    elif(numero > 0 and numero <=9):
        numero = '000' + str(numero)
        print(f'O numero {numero} tem: ')
        print(f'{numero[3]} unidades')
        print('0 dezenas')
        print('0 centenas')
        print('0 milhar')
    
    elif(numero >= 10 and numero <= 99):
        numero = '00' + str(numero)
        print(f'O numero {numero} tem: ')
        print(f'{numero[3]} unidades')
        print(f'{numero[2]} dezenas')
        print('0 centenas')
        print('0 milhar')
    
    elif(numero >= 100 and numero <= 999):
        numero = '0' + str(numero)
        print(f'O numero {numero} tem: ')
        print(f'{numero[3]} unidades')
        print(f'{numero[2]} dezenas')
        print(f'{numero[1]}0 centenas')
        print('0 milhar')   

    else:
        numero = str(numero)
        print(f'O numero {numero} tem: ')
        print(f'{numero[3]} unidades')
        print(f'{numero[2]} dezenas')
        print(f'{numero[1]} centenas')
        print(f'{numero[0]} milhar')        