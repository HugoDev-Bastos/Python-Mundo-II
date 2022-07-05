# Crie um programa que faça o computador jogar Jokempô com você
# Pedra papel Tisoura

from ast import And
from random import randint

pedra = 1
papel = 2
tisoura = 3

computador = randint(1,3)

print("-=-"*10)
print('[1] - Pedra \n[2] - Papel \n[3] - Tesoura')
print("-=-"*10)
jogador = int(input('Faça sua jogada: '))
print("-=-"*10)

if computador == 1:
    maoComputador = 'Pedra'
elif computador == 2:
    maoComputador = 'Papel'
elif computador == 3:
    maoComputador = 'Tesoura'

print('Computador: {}'.format(maoComputador))
print("-=-"*10)


if computador == 1 and jogador == 1 or computador == 2 and jogador == 2 or computador == 3 and jogador == 3:
    print('EMPATE')
elif computador == 1 and jogador == 3:
    print('Você perdeu! Pedra Ganha de Tesoura!')
elif computador == 2 and jogador == 1:
    print("Você Perdeu! Papel ganha de Pedra!")
elif computador == 3 and jogador == 2:
    print("Você Perdeu! Tesoura ganha de Papel!")



# pedra ganha de tesoura
# tesoura ganha de papel
# papel ganha de pedra

