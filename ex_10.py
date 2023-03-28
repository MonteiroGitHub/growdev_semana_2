#Exercício 10
#Após construir o programa anterior, crie mais duas versões dele para prever as seguintes situações:
#a) Um aluno pode ficar em recuperação se possuir frequência suficiente 
# (superior a 75%) e média superior a 5 mas inferior a 7;
# b) Caso um aluno reprove por média e faltas, sua situação deve ser
# “Reprovado por Média e Faltas” (ao invés de simplesmente
# “Reprovado por Faltas” como antes).


b1 = float(input('Digite a nota do primeiro bimestre: '))
b2 = float(input('Digite a nota do segundo bimestre: '))
b3 = float(input('Digite a nota do terceiro bimestre: '))
b4 = float(input('Digite a nota do quarto bimestre: '))

aulas_totais = int(input('Digite o numero total de aulas: '))
faltas = int(input('Digite quantas aulas o aluno faltou: '))

if (b1 + b2 + b3 + b3)/4 >= 5.00    and     (b1 + b2 + b3 + b3)/4 < 7.00       and     faltas <= (aulas_totais * 0.25):
        print('O aluno pode fazer recuperação!')
        
else:

    if (b1 + b2 + b3 + b3)/4 >= 7.00    and     faltas <= (aulas_totais * 0.25):
        print('O aluno esta aprovado!')
        
    else:
        print('O aluno esta reprovado por média e faltas!')