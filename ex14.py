cont = 0
n1 = "efewf"
soma = 0
media = 0
while n1!=0:
    cont = cont + 1
    n1 = int(input('Digite o numero :'))
    soma += n1
    media = soma/cont   
    print(n1)
print('Foram digitados {} numeros'.format(cont))
print('A soma é : {}'.format(soma))
print('A media é : {}'.format(media))