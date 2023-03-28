#Exercício 08
#Faça um programa para ler a quantidade adquirida e o preço unitário de um produto.
#a) Calcular e escrever o total
#       total = quantidade adquirida * preço unitário
#b) Leia o desconto sobre a compra e calcule.
#           total a pagar = total - desconto
#c) Sabendo-se que:
#(1) Se quantidade <= 5 o desconto será de 2%.
#(2) Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
#(3) Se quantidade > 10 o desconto será de 5%


quantidade = int(input('Digite a quantidade adquirida: '))      

valor_unid = float(input('Digite o valor da unidade: '))        #Float já que o valor pode vir com casa decimal   

valor_sem_desconto = quantidade * valor_unid

if quantidade < 1:
    print('Quantidade inválida!')

else:
    if quantidade == 1:     #criei este if pois quando eu colocava o valor 1, eu respondia no plural em todos os outros, porém, 1 quantidade é no singular. Não sei se tinha um método mais facil ou prático para corrigir este detalhe.
        
        valor_desconto2 =valor_sem_desconto - (valor_sem_desconto * 0.02)       #Se quantidade <= 5 o desconto será de 2%.
        print(f'{quantidade: .0f}, custa o valor total de R${valor_sem_desconto}. Com desconto, o total a ser pago é de R${valor_desconto2}')
    
    elif quantidade > 1      and     quantidade  <= 5 :     #Se quantidade <= 5 o desconto será de 2%.
        
        valor_desconto2 =valor_sem_desconto - (valor_sem_desconto * 0.02) 
        print(f'{quantidade: .0f}, custam o valor total de R${valor_sem_desconto}. Com desconto, o total a ser pago é de R${valor_desconto2}')

    elif quantidade > 5     and     quantidade <= 10:       #Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
        
        valor_desconto3 = valor_sem_desconto - (valor_sem_desconto * 0.03)
        print(f'{quantidade: .0f}, custam o valor total de R${valor_sem_desconto}. Com desconto, o total a ser pago é de R${valor_desconto3}')
    
    elif quantidade > 10:
        
        valor_desconto5 = valor_sem_desconto - (valor_sem_desconto * 0.05)      #Se quantidade > 10 o desconto será de 5%.
        print(f'{quantidade: .0f}, custam o valor total de R${valor_sem_desconto}. Com desconto, o total a ser pago é de R${valor_desconto5}')