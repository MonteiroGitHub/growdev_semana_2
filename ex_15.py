#Exercício 15
# Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento
# Entre 9.0 e 10.0 Conceito A
# Entre 7.5 e 8.9 B
# Entre 6.0 e 7.4 C
# Entre 4.0 e 5.9 D
# Entre 0 e 3.9 E
# O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem:
#a) APROVADO se o conceito for A, B ou C.
#b) REPROVADO se o conceito for D ou E.



n1 = float(input('Digite a nota da sua primeira prova(de 1 a 10): '))
n2 = float(input('Digite a nota da sua segunda prova(de 1 a 10): '))


if n1 < 0 or n2 < 0 :
    
    print('Digite uma nota válida')


elif n1 > 10 or n2 > 10:
    
    print('Digite uma nota válida')
    

else:
    
    
    if (n1 + n2 )/ 2 >= 9.0:
        
        conceito = 'A'
        aluno = 'APROVADO'
        print(f'O aluno esta {aluno} com conceito {conceito}, por ter a média de {(n1 + n2)/2}')
    
    
    elif (n1 + n2 )/ 2 < 9.0   and     (n1 + n2 )/ 2 >= 7.5:
        
        aluno = 'APROVADO'
        conceito = 'B'
        print(f'O aluno esta {aluno} com conceito {conceito}, por ter a média de {(n1 + n2)/2}')
    
    elif (n1 + n2 )/ 2 < 7.5   and     (n1 + n2 )/ 2 >= 6.0:
        
        aluno = 'APROVADO'
        conceito = 'C'
        print(f'O aluno esta {aluno} com conceito {conceito}, por ter a média de {(n1 + n2)/2}')
        
    
    elif (n1 + n2 )/ 2 < 6.0   and     (n1 + n2 )/ 2 >= 4.0:
        
        aluno = 'REPROVADO'
        conceito = 'D'
        print(f'O aluno esta {aluno} com conceito {conceito}, por ter a média de {(n1 + n2)/2}')
        
    
    else:
        
        aluno = 'REPROVADO'
        conceito = 'E'
        print(f'O aluno esta {aluno} com conceito {conceito}, por ter a média de {(n1 + n2)/2}')