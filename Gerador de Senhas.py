import random

print('Bem vindo ao Gerador de Senhas')

chars = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ!@#$%&*0123456789.,:;+-'

number = input('Quantidade de senhas para gerar: ')
number = int(number)
# cuidado ao escrever "Length, pois eu escrevi uma palavra errada e fez com que as senhas não aparececem"
length = input('Tamanho da sua senha: ')
length = int(length)

print('\ aqui esta suas senhas')

for pwd in range(number): 
    senhas = ''
    for c in range(length):
        senhas += random.choice(chars)
    print(senhas)