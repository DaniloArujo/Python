import random

while True:
    print('[1] Pedra')
    print('[2] Papel')
    print('[3] tesoura')
    jogada = int(input('Escolha sua opção: '))
    
    jogadaslista = ['Pedra', 'Papel', 'Tesoura']
    comp = random.choice(jogadaslista)

    if jogada < 1 or jogada > 3 :
        print('Jogada inválida')

    elif jogada == 1  and comp == 'Pedra' :
        print('###############################################################')
        print('Computador jogou Pedra')
        print('Você jogou pedra')
        print('\nEmpate! \n')
        print('###############################################################')

    elif jogada == 1 and comp == 'Papel' :
        print('###############################################################')
        print('Computador jogou Papel')
        print('Você jogou pedra')
        print('\nVocê perdeu! \n')
        print('###############################################################')

    elif jogada == 1 and comp == 'Tesoura' :
        print('###############################################################')
        print('Computador jogou Tesoura')
        print('Você jogou pedra')
        print('\nVocê ganhou! \n')
        print('###############################################################')

    elif jogada == 2 and comp == 'Pedra' :
        print('###############################################################')
        print('Computador jogou Pedra')
        print('Você jogou papel')
        print('\nVocê ganhou! \n')
        print('###############################################################')
    
    elif jogada == 2 and comp == 'Papel' :
        print('###############################################################')
        print('Computador jogou Papel')
        print('Você jogou papel')
        print('\nEmpate! \n')
        print('###############################################################')

    elif jogada == 2 and comp == 'Tesoura' :
        print('###############################################################')
        print('Computador jogou Tesoura')
        print('Você jogou papel')
        print('\nVocê perdeu! \n')
        print('###############################################################') 

    elif jogada == 3 and comp == 'Pedra' :
        print('###############################################################')
        print('Computador jogou Pedra')
        print('Você jogou tesoura')
        print('\nVocê perdeu! \n')
        print('###############################################################')
    

    elif jogada == 3 and comp == 'Papel' :
        print('###############################################################')
        print('Computador jogou Papel')
        print('Você jogou tesoura')
        print('\nVocê ganhou! \n')
        print('###############################################################')

    elif jogada == 3 and comp == 'Tesoura' :
        print('###############################################################')
        print('Computador jogou Tesoura')
        print('Você jogou tesoura')
        print('\nEmpate! \n')
        print('###############################################################')   