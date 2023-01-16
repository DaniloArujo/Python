#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preco = float(input('Valor do produto: '))

desconto = float(input('Valor do desconto: '))

print(f'O valor Final do produto é {preco - (preco * (desconto/100))}')