 

frase = 'Testando o tratamento de strings em Python'

print(frase)


#selecionando uma letra
print(frase[9])

#selecionando parte da string. sempre incrementar o segundo índice para pegar certinho.
print(frase[0:8])

#selecionar parte da string pulando de dois em dois
print(frase[0:40:2])

#recorta toda a string antes do indice selecionado
print(frase[:5])

#recorta toda a string após o indice selecionado
print(frase[5:])

#A mesma linha de raciocinio vale para indices com três valores
print(frase[::2])


#comprimento da string -> metodo len, de lenght
print(len(frase))

#para contar a quantidade de palavras ou de um determinado caractere 
print(frase.count('o'))
print(frase.count('tratamento'))

#A contagem pode ser feita com fatiamento. note que agora os indices são separados por vírgulas
print(frase.count('o',0,15))

#funcionalidade que mostra o indice da primeira palavra ou letra 
print(frase.find('tame'))

#replace 
print(frase.replace(' ','*'))

# capitalize transforma todos os caracteres em minusculos, exceto o primeiro
print(frase.capitalize())

#title converte todas as letras iniciais das palavras em maiúsculas
print(frase.title())

#strip remove todos os espaços em branco no inicio e no fim da string
frase2 = '     teste      '
print(frase2)
print(frase2.strip())

#algumas funcionalidades do python permite adicionar a letra r, que direciona o comando a direita ou L que direciona a esquerda
print(frase2.rstrip())
print(frase2.lstrip())

#split transforma uma string em várias, usando com parametro os espaços
frase = frase.split()
print(frase)
print(frase[2][0])

#join serve para juntar as diferentes listas em uma string
frase = '-'.join(frase)
print(frase)

#verificar se a palavra está dentro da frase (retorna boolean)
print('tratamento' in frase)