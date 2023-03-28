#Exercício 05
#Uma empresa vende um produto a R$5,40 a unidade. Sabendo-se que existe um desconto acumulado de 0,5% do valor total da compra a cada centena comprada deste produto. Escreva um programa que receba a quantidade comprada desse produto e informe.
#a) O valor total da compra (sem o desconto)
#b) A quantidade de centenas compradas desse produto
#c) O desconto em R$.
#d) O valor total da compra (com desconto)

#Levando em consideração que 0.5% == 0.005

quantidade_pedida = int(input('DIgite quanto do nosso produto o senhor quer: '))
produto = 5.40


valor_sem_desconto = quantidade_pedida * produto

print(f'O valor sem desconto é: R${valor_sem_desconto: .2f}')

if quantidade_pedida % 100 == 0 or quantidade_pedida >= 100:
    centena = quantidade_pedida // 100
    desconto = (centena * valor_sem_desconto) * 0.005
    valor_com_desconto = valor_sem_desconto - desconto
    
    print(f'Quantidade de centenas compradas:{centena}')
    print(f'O valor do desconto é de R${desconto: .2f}')
    print(f'O valor a ser pago já com o desconto é de R${valor_com_desconto: .2f}')
    #Ou print(f'A quantidade de centenas compradas ({centena}) dará um desconto de R${desconto: .2f}, logo o valor total a ser pago é de R${valor_com_desconto: .2f}')
elif quantidade_pedida > 0 and quantidade_pedida <= 99: 
    print('Voce não atingiu a quantidade mínima de compras para ter desconto, por favor pague o valor sem desconto.')
