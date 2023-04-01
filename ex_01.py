#Exercício 01
#Conversão de graus Celsius para Fahrenheit – Crie um programa que converta graus Celsius em Fahrenheit
#O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, em seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse programa, modifique-o para que converta graus Fahrenheit em graus Celsius.

#Versão de Celcius para Fahrenheit
temp = float(input('Digite a temperatura em Celcius: '))

nova_temp = (9/5*temp) + 32

print(f'{temp: .1f}°C em Fahrenheit é {nova_temp: .1f}°F ')

#Versão de Fahrenheit para Celcius

temp = float(input('Digite a temperatura em Fahrenheit: '))

nova_temp = (temp - 32) / 1.8

print(f'{temp: .1f}°F em Celcius é {nova_temp: .1f}°C')
