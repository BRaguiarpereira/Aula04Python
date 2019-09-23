v = int(input('Digite valor :'))
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while v!=0:
    if v>=50:
        v = v-50
        cont = cont + 1
    elif v>=20:
        v = v-20
        cont1 = cont1 + 1
    elif v>=10:
        v = v-10
        cont2 = cont2 + 1 
    elif v>=4:
        v = v-4
        cont3 = cont3 + 1  
    elif v>=1:
        v = v-1
        cont4 = cont4 + 1       
    print(v)
print('Quantidade de notas de 50 reais foram : {}'.format(cont))
print('Quantidade de notas de 20 reais foram : {}'.format(cont1))
print('Quantidade de notas de 10 reais foram : {}'.format(cont2))
print('Quantidade de notas de 4 reais foram : {}'.format(cont3))
print('Quantidade de notas de 1 real foram : {}'.format(cont4))

        