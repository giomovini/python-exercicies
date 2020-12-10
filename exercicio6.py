#Faça um Programa que peça dois números e imprima o maior deles.

a = int(input('escreva um número:'))
b = int(input('escreva outro número'))

if a > b:
    print(f'O número {a} é maior que o número {b}')
else:
    print(f'O número {a} é menor que o número {b}')