#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


ano_atual = 2023
aniversario = int(input('Você nasceu em qual ano ? '))

if ano_atual - aniversario == 18:
    print(f'Quem nasceu em {aniversario} tem {ano_atual - aniversario} anos em {ano_atual}')
    print(f'Este você deve se alistar este ano')
    
if ano_atual - aniversario < 18:
    print(f'Quem nasceu em {aniversario} tem {ano_atual - aniversario} anos em {ano_atual}')
    print(f'Você deve se alistar em {(18 - (ano_atual - aniversario)) + ano_atual}')

if ano_atual - aniversario > 18:
    print(f'Quem nasceu em {aniversario} tem {ano_atual - aniversario} anos em {ano_atual}')
    print(f'Voce deveria ter se alistado em {ano_atual - ((ano_atual - aniversario) - 18)}')


 