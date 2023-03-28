#Exercício 14
# As Organizações XTC resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calcula os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#a) salários até R$ 280,00 (incluindo): aumento de 20%
#b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
#c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
#d) salários de R$ 1500,00 em diante: aumento de 5%
#Após o aumento ser realizado informe na tela:
#a) o salário antes do reajuste;
#b) o percentual de aumento aplicado;
#c) o valor do aumento;
#d) o novo salário, após o aumento


salario = float(input('Digite seu sálario '))

if salario <= 0:
    print('Digite um salário válido')

else:

    if salario <= 280.00:
        aumento = 0.20
        reajuste = salario * aumento
        novo_salario = salario + reajuste
        print(f'O seu salário antes do aumento era de R${salario: .2f}, com o aumento de 20%, seu salário recebeu um aumento de R${reajuste: .2f}, assim, seu novo salário passa a ser de R${novo_salario: .2f}')
        
    elif salario > 280.00      and     salario <= 700.00:
        aumento = 0.15
        reajuste = salario * aumento
        novo_salario = salario + reajuste
        print(f'O seu salário antes do aumento era de R${salario: .2f}, com o aumento de 15%, seu salário recebeu um aumento de R${reajuste: .2f}, assim, seu novo salário passa a ser de R${novo_salario: .2f}')
    
    elif salario > 700.00      and     salario <= 1500.00:
        aumento = 0.10
        reajuste = salario * aumento
        novo_salario = salario + reajuste
        print(f'O seu salário antes do aumento era de R${salario: .2f}, com o aumento de 10%, seu salário recebeu um aumento de R${reajuste: .2f}, assim, seu novo salário passa a ser de R${novo_salario: .2f}') 
        
    else:
        aumento = 0.05
        reajuste = salario * aumento
        novo_salario = salario + reajuste
        print(f'O seu salário antes do aumento era de R${salario: .2f}, com o aumento de 5%, seu salário recebeu um aumento de R${reajuste: .2f}, assim, seu novo salário passa a ser de R${novo_salario: .2f}')  
