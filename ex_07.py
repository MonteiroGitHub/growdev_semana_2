#Exercício 07
#Faça um programa para ler a temperatura atual e conforme leitura, imprima o resultado de acordo com a tabela abaixo. Temperatura Resultado
# até 15º Muito frio
#de 16º à 22º Frio
#de 23º à 26º Agradável
#de 27º à 30º Quente
#31º ou mais Muito quente


def tem_casas_decimais(temperatura):
    return temperatura != int(temperatura)

temperatura = float(input('Digite a temperatura: '))

if tem_casas_decimais(temperatura):
    
    if temperatura <= 15     and     tem_casas_decimais(temperatura):
        print(f'{temperatura: .1f}° é muito frio!')
        

    elif temperatura > 15   and   temperatura <= 22      and     tem_casas_decimais(temperatura):
        print(f'{temperatura: .1f}° é frio!')
        
    elif temperatura >= 23   and   temperatura <= 26      and     tem_casas_decimais(temperatura):
        print(f'{temperatura: .1f}° é agradável!')

    elif temperatura >= 27   and   temperatura <= 30      and     tem_casas_decimais(temperatura):
        print(f'{temperatura: .1f}° é quente!')

    elif temperatura >= 31       and     tem_casas_decimais(temperatura):
        print(f'{temperatura: .1f}° é muito quente!')
        
else:

    if temperatura <= 15 :
        print(f'{temperatura: .0f}° é muito frio!')
        

    elif temperatura > 15   and   temperatura <= 22:
        print(f'{temperatura: .0f}° é frio!')
        
    elif temperatura >= 23   and   temperatura <= 26:
        print(f'{temperatura: .0f}° é agradável!')

    elif temperatura >= 27   and   temperatura <= 30:
        print(f'{temperatura: .0f}° é quente!')

    elif temperatura >= 31:
        print(f'{temperatura: .0f}° é muito quente!')