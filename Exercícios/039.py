# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date

nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se Alista IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Voé ainda não tem 18 anos. Ainda faltam {} ano para o Alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistameto será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se Alistado há {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamto foi em {}'.format(ano))