#Exercício 12
#Construa um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.


dia = int(input('Informe um dia(1 a 31): '))
mes = int(input('Informe um mês(1 a 12): '))
ano = int(input('Informe um ano: '))

if dia < 1     or     dia > 31:
    
    print('Data inválida, por favor escreve um número de dias válido! ')
    
elif mes < 1    or    mes > 12:
    
    print('Data inválida, por favor escreve um número de meses válido! ')
    
else:
    
    if ano % 4 != 0     and     dia == 28       and     mes == 2:
    
        print(f'A data do próximo dia é 1/{mes + 1}/{ano}!')
        
    elif ano % 4 == 0     and     dia == 29       and     mes == 2:
        
        print(f'A data do próximo dia é 1/{mes + 1}/{ano}!')
        
    elif ano % 4 != 0     and     dia == 29       and     mes == 2:
    
        print(f'A data ({dia}/{mes}/{ano}) é inválida!')
        
    elif ano % 4 != 0     and     dia >= 29       and     mes == 2:
    
        print('Data inválida!')
    
    else:
    
        if dia == 31    and     mes == 12:
    
            print(f'A próxima data após ({dia}/{mes}/{ano}) é {1}/{1}/{ano+1}!')
            
        if dia == 31    and     (mes != 2      or      mes != 4    or      mes != 6    or      mes != 9    or      mes != 11):
    
            print(f'A próxima data após ({dia}/{mes}/{ano}) é {1}/{mes + 1}/{ano}!')
            
        elif dia == 30      and      (mes == 4    or      mes == 6    or      mes == 9    or      mes == 11):
    
            print(f'A próxima data após ({dia}/{mes}/{ano}) é {1}/{mes + 1}/{ano}!')
            
        else:
    
            print(f'A próxima data após ({dia}/{mes}/{ano}) é {dia+1}/{mes}/{ano}!')