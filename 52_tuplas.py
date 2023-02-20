
lanche = ('hamburger','suco','pizza','pudim')

print(lanche)

print(lanche[2])


#lembrar de que o ultimo numero é ignorado
print(lanche[0:2])

print(lanche[1:])

#ultimo elemento (indice ao contrário)
print(lanche[-1])

print(len(lanche))

for item in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[item]} na posição {item}')

for elem in lanche:
    print(elem)

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')


#dá o print em ordem alfabetica
print(sorted(lanche))


##########################################################################

#No caso da soma de tuplas acontece uma concatenação. a ordem da soma interfere no resultado final.
#note que em caso de soma os numeros repitidos são mantidos.

a = (5,2,4,2)
b = (1,8,6)

print(a + b)
print(b + a)

print((a+b).count(2))

#o comando index pergunta em qual posição está o caractere específico

print((a+b).index(8))

#posso usar o comando del(tupla) para apagar a tupla e criar uma nova