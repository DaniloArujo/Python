#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


listaPrincipal = []
listaPar = []
listaImpar = []

while True:
    variavel = int(input('Digite um valor: '))

    if variavel  == 0 :
        break

    listaPrincipal.append(variavel)


for elem in listaPrincipal:
    if elem %2 == 0:
        listaPar.append(elem)
    else:
        listaImpar.append(elem)

print(listaPrincipal)
print(listaPar)
print(listaImpar)