# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem: 
# - O primeiro é maior
# - O segundo é maior
# - Não existe valo maior, os dois são iguais


n1 = int(input('Primeiro Número: '))
n2 = int(input('Sgundo Número: '))


if n2 > n1:
    print('O Segundo número {} é maior!'.format(n2))
elif n1 > n2:
    print('O primeiro número {} é maior!'.format(n1))
else:
    print('Não existe valor maior, os dois são iguais!')
