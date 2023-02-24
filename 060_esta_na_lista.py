#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = []

while True:
    valor = int(input('Digite um valor, ou digite zero para parar o programa: '))

    if valor == 0:
        break

    if valor in lista:
        print('Valor já está na lista')
    else:
        lista.append(valor)


print(sorted(lista))