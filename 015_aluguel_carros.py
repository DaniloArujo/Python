#Escreva um programa que pergunte a quantidade de Km percorridos por um 
#carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
#que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input('Insira a quantidade de dias: '))
kilometragem = float(input('Insira a kilometragem: '))


valordia = dias * 60
valorkm = kilometragem * 0.15

print(f'O preço a ser pago é de {valordia + valorkm }')