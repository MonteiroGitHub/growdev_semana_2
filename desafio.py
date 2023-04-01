#numero_calculo = int(input("Digite um número para calcular a sequência: "))
#guess1 = int(input("Digite o primeiro número da sequência: "))
#guess2 = int(input("Digite o segundo número da sequência: "))
#guess3 = int(input("Digite o terceiro número da sequência: "))

#definir a "semente" do gerador de números pseudoaleatórios
seed = 123456789

#gerar três números pseudoaleatórios entre 0 e 9
num1 = (seed * seed) // 100 % 10000 % 10
seed = num1 * num1
num2 = (seed * seed) // 100 % 10000 % 10
seed = num2 * num2
num3 = (seed * seed) // 100 % 10000 % 10

#pedir para o usuário fornecer um palpite com três números
guess = input("Digite um palpite com três números (entre 0 e 9): ")

#verificar quantos números foram acertados
points = 0

if guess[0] == str(num1) or guess[1] == str(num1) or guess[2] == str(num1):
    points += 10

elif guess[0] == str(num2) or guess[1] == str(num2) or guess[2] == str(num2):
        points += 10

elif guess[0] == str(num3) or guess[1] == str(num3) or guess[2] == str(num3):
    points += 10

elif guess[0] == str(num1) and guess[1] == str(num2) and guess[2] == str(num3):
    points = 1000000

elif guess[0] == str(num2) and guess[1] == str(num1) and guess[2] == str(num3):
    points = 1000

elif guess[0] == str(num2) and guess[1] == str(num3) and guess[2] == str(num1):
    points = 1000

elif guess[0] == str(num3) and guess[1] == str(num1) and guess[2] == str(num2):
    points = 1000

elif guess[0] == str(num3) and guess[1] == str(num2) and guess[2] == str(num1):
    points = 1000

#imprimir o resultado
print("Os números sorteados foram:", num1, num2, num3)
print("Seu palpite foi:", guess)
print("Você acertou", points, "número(s).")