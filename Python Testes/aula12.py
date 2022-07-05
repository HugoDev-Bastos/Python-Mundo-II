nome = str(input('Qua é o seu nome? '))
if nome ==  'Hugo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino!')

print('Tenha um bom dia, {}!'.format(nome))