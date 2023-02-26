pessoas = list()


danilo = ['Danilo', 'Araujo', 'Mota', '28','M']
eduarda = ['Maria', 'Eduarda', 'siqueira', '24','F']


#lembar de colocar um [:] quando não quiser uma ligação entre a lista orignal e a cópia
pessoas.append(danilo[:])
pessoas.append(eduarda[:])

print(pessoas)

danilo[3] = '29'
print(danilo)
print(pessoas)

pessoas[0][3] = 29
print(pessoas)

print(pessoas[0])