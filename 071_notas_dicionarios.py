

aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Nota'] = float(input('Nota: '))

if aluno['Nota'] < 7:
    aluno['situacao'] = 'reprovado'

else:
    aluno['situacao'] = 'aprovado'
   
print(f'O aluno {aluno["Nome"]} tirou {aluno["Nota"]} na prova e está {aluno["situacao"]}.')