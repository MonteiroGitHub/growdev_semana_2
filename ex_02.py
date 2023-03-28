#Exercício 02
#Escreva um programa que receba um número e escreva “Par” caso esse número seja par e escreva “Impar” caso esse número seja impar.

#Para saber se um número é impar ou par levamos em consideração o resto dele, se o resto for 0 é par, se for 1 é impar

valor = int(input('Informe um número: '))

resto = valor % 2

if resto == 0:
    print(f'{valor} é par')
else:
    print(f'{valor} é impar')