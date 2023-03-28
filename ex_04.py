#Exercício 04
#Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
#CENTENA = x
#DEZENA = x
#UNIDADE = x
#Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.

#Aqui caso o usuário digite um numero menor que 100 ele também terá resultados.
numero = int(input('Digie um número de até 3 digitos (ex 999): '))

if numero >= 1000:
    print('digite um número de apenas 3 digitos, conforme discrito no exemplo')

if numero >=100 and numero <= 999:
    centena = numero // 100         # // corresponde a divisão inteira, ex: 7 // 2 = 3
    dezena = (numero % 100) // 10   # % corresponde a pegar o resto da divisão e em seguida pegar e dividir por 10
    unidade = numero % 10           # % corresponde a pegar o resto da divisão
       
    print(f'a centena é {centena}, a dezena é {dezena} e a unidade é {unidade}.')
    
elif numero <100 and numero >= 10:
    dezena = (numero % 100) // 10
    unidade = numero % 10
    print(f'este número não contém centena, a dezena é {dezena} e a unidade é {unidade}.')
    
elif numero <=9 and numero >=0:
    unidade = numero % 10
    print(f'este número não contém centena e nem dezena, a unidade é {unidade}.')