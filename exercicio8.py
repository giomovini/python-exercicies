#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite F-para Feminino ou (M) para Masculino: '))

if sexo == 'M':
    print('Sexo masculino')
elif sexo == 'F':
    print('Sexo feminino')
else:
    print('Sexo inválido')