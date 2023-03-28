#Exercício 13
#Construa um programa que, a partir do valor do comprimento dos três lados de um triângulo, classifique-o em equilátero, isósceles ou escaleno. Lembre, um triângulo é equilátero quando o comprimento de todos os seus lados for igual, é isósceles quando apenas um dos lados tiver comprimento diferente e é escaleno quando todos os lados tiverem comprimentos diferentes dos demais lados.


l1 = float(input('Informe o comprimento primeiro lado do triângulo: '))
l2 = float(input('Informe o comprimento segundo lado do triângulo: '))
l3 = float(input('Informe o comprimento terceiro lado do triângulo: '))


if l1 == l2     and     l2 == l3:
    
    print('Este triângulo é um equilátero')
    
elif l1 == l2       or      l2 == l3        or      l1 == l3:
    
    print('Este triângulo é um isósceles')

else:
    
    print('Este triângulo é um escaleno')