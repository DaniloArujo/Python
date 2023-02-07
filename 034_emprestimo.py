#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


valor = int(input('Digite o valor da casa: '))

salario = int(input('Agora digite o seu salário: '))

parcelas = int(input('Pretende dividir em quantas vezes? '))

valor_parcela = valor / (parcelas * 12)

if valor_parcela > salario / 100 * 30 :
    print('Negado')

elif valor_parcela == salario / 100 * 30:
    print('Aprovado')

else:
    print('Aprovado com sobras')



print(valor_parcela)