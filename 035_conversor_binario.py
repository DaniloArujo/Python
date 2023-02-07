#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


num = int(input('Digite um valor: '))

opcao = int(input('Digite 1 para converter em binario, 2 para octal e 3 para hexadecimal: '))

if opcao < 1 or opcao > 3:
    print('opção inválida')

elif opcao == 1:
    print(bin(num)[2:])

elif opcao == 2:
    print(oct(num)[2:])

elif opcao == 3:
    print(hex(num)[2:])