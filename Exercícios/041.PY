# A Confederação nacional de nataçaõ precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a sua idade.

# Até 9 anos: Mirim
# Até 14 anos: Infantial
# até 19 anos: Junior
# até 20 anos: Sênior
# acima: Master

nascimento = int(input('Data de nascimento: '))

if nascimento <= 9:
    print('Mirim')
elif nascimento > 9 and nascimento <= 14:
    print("Infantil")
elif nascimento > 14 and nascimento <= 19:
    print('Junior')
elif nascimento > 19 and nascimento <= 20:
    print("Sênior")
else:
    print("Master")


