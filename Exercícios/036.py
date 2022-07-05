#Escreva um programa para aprov\r o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela nçao pode exceder 30% do salaário ou então o empréstimo será negado.

casa = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa / (anos * 12)
mínimo = salário * 30/100

print("Para pagar uma casa de R${:0.2f} em {} anos, a prestaçãp será de R${:0.2f}".format(casa,anos, prestação))


if prestação <= mínimo:
    print("Empréstimo pode ser Concedido!")
else:
    print("Empréstimo negado!")



