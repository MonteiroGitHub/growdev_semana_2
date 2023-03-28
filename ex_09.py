#Exercício 09
#Numa determinada escola, os critérios de aprovação são os seguintes:
#a) O aluno deve ter, no máximo, 25% de faltas;
#b) A nota final deve ser igual ou superior a 7,00.
#Construa um programa para ler as notas que um aluno tirou nos 4 bimestres, o número total de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por média”, considerando que a reprovação por faltas se sobrepõe a reprovação por nota.


b1 = float(input('Digite a nota do primeiro bimestre: '))
b2 = float(input('Digite a nota do segundo bimestre: '))
b3 = float(input('Digite a nota do terceiro bimestre: '))
b4 = float(input('Digite a nota do quarto bimestre: '))

aulas_totais = int(input('Digite o numero total de aulas: '))
faltas = int(input('Digite quantas aulas o aluno faltou: '))

if (b1 + b2 + b3 + b3)/4 >= 7.00    and     faltas <= (aulas_totais * 0.25):
    print('O aluno esta aprovado!')

elif faltas > (aulas_totais * 0.25):
    print('O aluno esta reprovado por faltas!')
    
else:
    print('O aluno esta reprovado por não ter média igual ou superior a 7.00!')