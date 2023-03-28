#Exercício 11
#Escreva um programa que peça ao usuário para fornecer um dia, mês e o ano arbitrários e determine se esses dados correspondem a uma data válida.Não deixe de considerar que existem meses com 30 e 31 dias, e que fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto. Considere que um ano é bissexto quando for divisível por 4.


dia = int(input('Informe um dia(1 a 31): '))
mes = int(input('Informe um mês(1 a 12): '))
ano = int(input('Informe um ano: '))

if dia < 1     or     dia > 31:
    
    print('Data inválida, por favor escreve um número de dias válido! ')
    
elif mes < 1    or    mes > 12:
    
    print('Data inválida, por favor escreve um número de meses válido! ')
    
else:
    
    if ano % 4 == 0     and     dia == 29       and     mes == 2:
        
        print('Data válida!')
    
    elif ano % 4 != 0     and     dia == 29       and     mes != 2:
        
        print('Data inválida, em ano bissexto somente fevereiro tem 29 dias!')
    
    elif ano % 4 != 0     and     dia == 29       and     mes == 2:
        
        print('Data inválida, fevereiro só tem 29 dias em ano bissexto!')
        
    elif ano % 4 != 0     and     dia == 28       and     mes == 2:
        
        print('Data válida!')
        
    else:
        
        if dia == 30    and     mes == 4    or      mes == 6    or      mes == 9    or      mes == 11:
            
            print('Data válida!')
            
        else:
            
            if dia == 31    and     mes != 2      or      mes != 4    or      mes != 6    or      mes != 9    or      mes != 11:
                
                print('Data válida!')
            
        
            
        