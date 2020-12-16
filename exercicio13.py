#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite seu nome [com mínimo de 4 caracteres]: '))
idade = int(input('idade: '))
salario = float(input('Salário : '))
sexo = input('Sexo "f" para feminino e "m" para masculino: ')
civil = input('s, c, v, d :')

while len(nome) <=3:
    nome = input('Seu nome deve conter mais que 3 caracteres: ')

while (idade < 0) or (idade > 150):
    idade = int(input('Você deve ter entre 0 e 150 anos: '))

while (salario < 0):
    salario = float(input('Seu salário deve ser maior que 0: '))

while (sexo!= 'f') and (sexo!= 'm'):
    sexo = input('Biológicamente você deve ser "f" ou "m" :')

while (civil!= 's') and (civil!= 'c') and (civil!= 'v') and (civil!= 'd'):
    civil = input('Deve ser s, c, v, d: ')

print('Cadastro concluido com sucesso!')