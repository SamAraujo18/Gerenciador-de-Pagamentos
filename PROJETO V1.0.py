from time import sleep
print('-=-' * 20)
nome = str(input('Digite seu nome para prosseguir: '))
print('-=-' * 20)
sleep(1.7)
print(f'Olá,\033[31m {nome}\033[m seja bem vindo ao caixa eletrônico \033[36monline\033[m da loja')
print('-=-' * 20)
sleep(3)
preco = float(input('Digite o preço do seu produto: R$'))
print('-=-' * 20)
print("""Selecione abaixo a forma de pagamento:

               [1] \033[1;97mÁ vista | \033[m\033[32mdinheiro/cheque \033[m= \033[33m10% de desconto\033[m
               [2] \033[1;97mÁ vista | \033[m\033[32mcartão \033[m= \033[33m5% de desconto\033[m
               [3] \033[1;97m2x no cartão | \033[m\033[33mpreço normal\033[m
               [4] \033[1;97m3x ou mais | \033[m\033[33m20% de juros\033[m
               """)
print('')
forma = input('Selecione a forma de pagamento: ')
print('')
if forma == '1':
    print(f'O Valor do produto á vista no dinheiro/cheque vai ficar em torno de \033[1;92mR${preco - (preco * 10/100):.2f}\033[m')
if forma == '2':
    print(f'O Valor do produto á vista no cartão vai ficar em torno de \033[1;92mR${preco - (preco * 5/100):.2f}\033[m')
if forma == '3':
    print(f'O Valor do produto em até 2x no cartão vai ficar em torno de \033[1;92mR${preco:.2f}\033[m no valor total')
if forma == '4':
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra sera parcelada em até \033[1;97m{parcela}x\033[m de \033[1;92mR${parcela/100 * (preco + (preco * 20 / 100)):.2f}\033[m')
    print(f'O produto vai custar \033[1;92mR${preco + (preco * 20 / 100):.2f}\033[m no valor final')
if forma >= '5':
    print('FORMA DE PAGAMENTO INVÁLIDA!!')
