
valorS = 0
valor1 = 0
valor2 = 0
valor4 = 0
valor5 = 0
valor9 = 0
codi = 'adas'
cont = 0
scont = -1
while codi!=0:
    codi = int(input('Digite o cod :'))
    if codi == 1 :
        q = float(input('Digite quantidade de produtos:'))
        valor1 = 0.50 * q
        cont = 1
    elif codi == 2 :
        q = float(input('Digite quantidade de produtos:'))
        valor2 = 1.00 * q
        cont = 1
    elif codi == 4 :
        q = float(input('Digite quantidade de produtos:'))
        valor4 = 4.00 * q
        cont = 1
    elif codi == 5 :
        q = float(input('Digite quantidade de produtos:'))
        valor5 = 7.00 * q
        cont = 1
    elif codi == 9 :
        q = float(input('Digite quantidade de produtos:'))
        valor9 = 8.00 * q
        cont = 1
    elif codi == 0 :
        print('Sua compra foi finalizada com Sucesso !!')
    else  :
        print('Sua anta esse produto está cadastrado seu retardado !!')
    scont += cont  
    valorS = valor1 + valor2 + valor4 + valor5 + valor9 
print('Voce comprou {} produtos ta podendo em ...'.format(scont))
print('Sua compra foi de {} reais'.format(valorS))
    






