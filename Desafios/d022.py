nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O nome {} possui {} letras'.format(dividido[0], len(dividido[0])))