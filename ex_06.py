#Exercício 06
#Escreva um programa que receba dois números, exiba as opções:
#a) 1 - adição
#b) 2 - subtração
#Então peça ao usuário para escolher uma das opções. Caso escolha a opção 1 o programa deve realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o programa deve realizar a subtração dos dois números lidos e exibir.


def tem_casas_decimais(n1): #A função tem_casas_decimais(depende de n1)
    return n1 != int(n1)    #Caso n1 seja diferente de inteiro(valor digitado) a função retornará True, mas se se for diferente, retornará False

def tem_casas_decimais2(n2): #A função tem_casas_decimais(depende de n2)
    return n2 != int(n2)     #Caso n2 seja diferente de inteiro(valor digitado) a função retornará True, mas se se for diferente, retornará False

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

operacao = int(input('Informe a operação solicitada 1-Adição ou 2-Subtração: '))

if operacao >= 3 or operacao <1:    #Se o usuário digitar um número maior/igual a 3 OU menor que 1 eu barro e o programa não continua
    print('Operação inválida!')

else:       #Se não, segue 
    
    
    if  operacao == 1 and tem_casas_decimais(n1) or tem_casas_decimais2(n2)    : #Se a operação for igual 1 e um dos dois digitos for True, eu ativo esse IF
        print (f'{n1: .2f} +{n2: .2f} é igual a {n1 + n2: .2f}')

    elif operacao == 2 and tem_casas_decimais(n1) or tem_casas_decimais2(n2)     : #Se a operação for igual 2 e um dos dois digitos for True, eu ativo esse ELIF
        print (f'{n1: .2f} -{n2: .2f} é igual a {n1 - n2: .2f}')



    if operacao == 1    and     not tem_casas_decimais(n1) and not tem_casas_decimais2(n2):#Se a operação for igual 1 e os dois digitos forem False, eu ativo esse IF
        print (f'{n1: .0f} +{n2: .0f} é igual a {n1 + n2: .0f}')

    elif operacao == 2 and   not tem_casas_decimais(n1) and not tem_casas_decimais2(n2):   #Se a operação for igual 2 e os dois digitos forem False, eu ativo esse ELIF
        print (f'{n1: .0f} -{n2: .0f} é igual a {n1 - n2: .0f}')  