#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angle = float(input('Digite o anglulo: '))

#primeiro converto em radianos

angle = math.radians(angle)


sen = math.sin(angle)
cos = math.cos(angle)
tan = math.tan(angle)

print(f'seno: {sen:.2f}, coseno: {cos:.2f}, tangente: {tan:.2f}')

#detalhe no arredondamento do format