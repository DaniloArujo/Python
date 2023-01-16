#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salario base: '))

porcentagem = float(input('Digite o valor do aumento: '))

print(f'O novo salário é de: {salario + (salario * porcentagem/100)}')