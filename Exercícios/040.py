# Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando uma mensagem no final, de acordo com a média atiginda:
# - Moédia abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input("Primeira nota: "))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media <= 5:
    print('Tirando {:.1f} e {:.1f} a média {:.1f} e o Aluno está REPROVADO!'.format(n1, n2, media))
elif media > 5 and media <= 6.9:
    print('Tirando  {:.1f} e {:.1f} a média {:.1f} e o Aluno está de RECUPERAÇÃO!'.format(n1, n2, media))
else: 
    print('Tirando  {:.1f} e {:.1f} a média {:.1f} e o Aluno está APROVADO!'.format(n1, n2, media))   