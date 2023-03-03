from time import sleep

print('-'*50)
print('BEM VINDO A LOCADORA BELAS ARTES')
print('-'*50)

catalogo = []
disponiveis = []
alugados = []


while True:
    print('[1] Cadastrar filme')
    print('[2] verificar catalogo')
    print('[3] filmes disponiveis')
    print('[4] filmes alugados')
    print('[5] alugar um filme')
    print('[6] fazer uma devolução')
    print('[7] Deletar um filme')
    print('[8] Sair do programa')
    
    print()
    opção = int(input('Escolha uma opção: '))
    
    #validação de dados
    if opção < 0 or opção > 8:
        print('Valor inválido')
        pass

    #menu sair do programa
    elif opção == 8:
        print('Obrigado pela preferência')
        print()
        break

    #menu adicionar filme
    elif opção == 1:
        filme = {}
        print('Caso queira voltar ao menu iniciar digite "cancelar" a qualquer hora')
        nome_temp = input('Digite o NOME do filme: ').upper()
        ano_temp = input('Digite o ANO do filme: ').lower()
        genero_temp = input('Digite o GENERO do filme: ').lower()
        diretor_temp = input('Digite o DIRETOR do filme: ').lower()

        if nome_temp == 'CANCELAR' or ano_temp == 'cancelar' or genero_temp == 'cancelar' or diretor_temp == 'cancelar':
            continue
        else:
            filme['titulo'] = nome_temp
            filme['ano'] = ano_temp
            filme['genero'] = genero_temp
            filme['diretor'] = diretor_temp
        

        catalogo.append(filme)
        disponiveis.append(filme)
        print(f'Voce acabou de cadastrar o filme {filme["titulo"]}')
        print()
        sleep(1)
        
        pass


    #menu verificar catalogo de filmes
    elif opção == 2:
        if len(catalogo) == 0:
            print('-'*50)
            print('CATALOGO VAZIO')
            print('-'*50)

        else:
            print('-'*50)
            print('CATALOGO DE FILMES')
            print('-'*50)
            for elem in range(len(catalogo)):
                print(f" [{elem}] {catalogo[elem]['titulo']}, {catalogo[elem]['ano']}, {catalogo[elem]['genero']}")
            print()
            sleep(1)


    #menu verificar catalogo de filmes disponiveis
    elif opção == 3:
        if len(disponiveis) == 0:
            print('-'*50)
            print('SEM FILMES DISPONÍVEIS')
            print('-'*50)

        else:
            print('-'*50)
            print('CATALOGO DE FILMES DISPONÍVEIS')
            print('-'*50)
            for elem in range(len(disponiveis)):
                print(f" [{elem}] {disponiveis[elem]['titulo']}, {disponiveis[elem]['ano']}, {disponiveis[elem]['genero']}")
            print()
            sleep(1)

    #menu lista filmes alugados
    elif opção == 4:
        if len(alugados) == 0:
            print('-'*50)
            print('SEM FILMES ALUGADOS')
            print('-'*50)
            print()
            sleep(1)

        else:
            print('-'*50)
            print('CATALOGO DE FILMES ALUGADOS')
            print('-'*50)
            for elem in range(len(alugados)):
                print(f" [{elem}] {alugados[elem]['titulo']}, {alugados[elem]['ano']}, {alugados[elem]['genero']}")
            print()
            sleep(1)


    #menu alugar filme 
    elif opção == 5:
        if len(disponiveis) == 0:
            print('-'*50)
            print('SEM FILMES DISPONÍVEIS PARA ALUGUEL')
            print('-'*50)
            print()
            sleep(1)

        else:
            print('-'*50)
            print('CATALOGO DE FILMES DISPONÍVEIS')
            print('-'*50)
            for elem in range(len(disponiveis)):
                print(f" [{elem}] {disponiveis[elem]['titulo']}, {disponiveis[elem]['ano']}, {disponiveis[elem]['genero']}")
            print()


            escolha = int(input('Escolha um filme de acordo com o indice: '))

            try:
                while True: 
                    confirmar = input(f'Voce deseja alugar o filme {disponiveis[escolha]["titulo"]}?[s/n] ').lower()

                    if confirmar == 's':
                        alugados.append(disponiveis[escolha])
                        del disponiveis[escolha]
                        print('Alugado com sucesso! ')
                        break
                    elif confirmar =='n':
                        break
                    else:
                        print('Comando inválido.')
                        print()
                        continue

            except:
                print('Erro ao alugar o filme')

            sleep(1)


    #Fazer uma devolução (alugados para disponiveis)
    elif opção == 6:
        if len(alugados) == 0:
            print('-'*50)
            print('SEM FILMES PARA DEVOLUÇÃO')
            print('-'*50)
            print()
            sleep(1)

        else:
            print('-'*50)
            print('ESCOLHA O FILME A SER DEVOLVIDO')
            print('-'*50)
            for elem in range(len(alugados)):
                print(f" [{elem}] {alugados[elem]['titulo']}, {alugados[elem]['ano']}, {alugados[elem]['genero']}")
            print()
            escolha = int(input('Escolha o filme de acordo com o indice: '))

            try:
                while True: 
                    confirmar = input(f'Voce deseja retornar o filme {alugados[escolha]["titulo"]}?[s/n] ').lower()

                    if confirmar == 's':
                        disponiveis.append(alugados[escolha])
                        del alugados[escolha]
                        print('Retornado com sucesso! ')
                        break
                    elif confirmar =='n':
                        break
                    else:
                        print('Comando inválido.')
                        print()
                        continue
            except:
                print('Erro ao retornar o filme')

            sleep(1)

           
           
    #Excluir um filme do catálogo
    elif opção == 7:
        print('-'*50)
        print('CATALOGO DE FILMES')
        print('-'*50)
        for elem in range(len(catalogo)):
            print(f" [{elem}] {catalogo[elem]['titulo']}, {catalogo[elem]['ano']}, {catalogo[elem]['genero']}")
        print()
        sleep(1)


        escolha = int(input('Escolha o filme a ser excluido de acordo com o índice: '))
        Deleted_film = catalogo[escolha]['titulo']
        
        if catalogo[escolha] in disponiveis:
            for elem in range(len(disponiveis)):
                if catalogo[escolha]['titulo'] == disponiveis[elem]['titulo']:
                    print('1')
                else:
                    print('2')



        else:
            print('Alugados')

        