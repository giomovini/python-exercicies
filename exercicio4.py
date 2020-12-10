#Faça um Programa que peça as 3 notas e mostre a média.
nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
nota3 = float(input('Escreva a terceira nota: '))
soma = nota1 + nota2 + nota3
media = soma / 3

print(f'A média entre {nota1}, {nota2} e a {nota3} é igual a {media}')