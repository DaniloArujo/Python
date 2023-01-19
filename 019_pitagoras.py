#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cateto01 = float(input('Qual é o comprimento do cateto oposto: '))
cateto02 = float(input('Qual é o comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(cateto01,2) + math.pow(cateto02,2))

# Ou posso usar o método math.hypot(x,y) que faz esse calculo diretamente


print(hipotenusa)