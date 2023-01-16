#Escreva um programa que converta uma temperatura digitando 
#em graus Celsius e converta para graus Fahrenheit.

temperatura = int(input('Digite A temperatura: '))

fahrenheit = ((9*temperatura)/5)+32

print(f'A temperatura de {temperatura} corresponde a {fahrenheit} em fahrenheit')