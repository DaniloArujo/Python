#Criar uma lista 

livros = ['O silmarillion','A sociedade do anél','As duas torres']

print('\n',livros)

print(livros[1:])

livros.append('O retorno do rei')

print(livros)

livros.insert(1,'O Hobbit')

print(livros)


#eliminar um item = 'lista.pop()' para eliminar o ultimo e 'lista.pop' para eliminar um específico, posso usar tambêm o comando 'del lista[3]' e tambêm posso usar o médoto 'lista.remove('exemplo')'. Nesse ultimo eu coloco no nome do item como parâmetro.



#para criar uma cópia de uma lista devemos fazer o seguinte:

a = [2,5,8,7]
b = a[:]

#caso o contrário faremos uma ligação entre as listas