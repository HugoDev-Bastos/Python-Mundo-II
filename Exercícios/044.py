# Elabore um programa que calcule o valora ser pago por um produto. Considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10 % de desc
# - À vista no cartão : 5% de des
# - em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
#

produto = float(input('Qual o valor do Produto R$: '))

print('-=-'*10 )
print(' Formas de Pagamentos')
print('-=-'*10 )
print('1 - À Vista Dinheiro/Cheque \n2 - À vista no cartão \n3 - Parcelado no Cartão')
print('-=-'*10 )

forma = int(input('Qual a forma de pagamento: '))

if forma == 1 :
    valor = produto - (produto * 10/100)
    print('O valor Total a pagar é de R${:0.2f}'.format(valor))
elif forma == 2:
    valor = produto - (produto * 5/100)
    print('O valor Total a pagar é de R${:0.2f}'.format(valor))
elif forma == 3:
    parcela = int(input("Quantidade de parcelas: "))

    if parcela <= 2:
        qtdpar = produto / parcela
        print("O Total a pagar é de R${} em x{} no Cartão".format(qtdpar, parcela))

    else: 
        novoValor = produto + ( produto * 20/100)
        parValor = novoValor / parcela
        print("O Total a pagar é de R${} em x{} no Cartão".format(parValor, parcela))
print("Obrigado, Volte sempre!")



        

    