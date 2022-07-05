# Escreva um prorama que leia um número inteteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcão = int(input('Sua opçao: '))

if opcão == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcão == 2:
    print('{} convertido para  OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcão == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida, Tente novamente!')