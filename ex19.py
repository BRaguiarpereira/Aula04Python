v = float(input('Digite valor :'))
con = 0
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
sc = 0
sc1 = 0
sc2 = 0
sc3 = 0
sc4 = 0
if v==0:
    print('Seu retardado não me deu nada e ainda quer troco !!asdhgqw')
else:
    while v!=0:
        if v>=100:
            v = v-100
            con = con + 1       
        elif v>=50:
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
        elif v>=0.50:
            v = v-0.50
            sc = sc + 1
        elif v>=0.10:
            v = v-0.10
            sc1 = sc1 + 1 
        elif v>=0.05:
            v = v-0.05
            sc2 = sc2 + 1
        elif v>=0.02:
            v = v-0.02
            sc3 = sc3 + 1
        elif v>=0.01:
            v = v-0.01
            sc4 = sc4 + 1         
    print('Quantidade de notas de 100 reais foram : {}'.format(con))     
    print('Quantidade de notas de 50 reais foram : {}'.format(cont))
    print('Quantidade de notas de 20 reais foram : {}'.format(cont1))
    print('Quantidade de notas de 10 reais foram : {}'.format(cont2))
    print('Quantidade de notas de 4 reais foram : {}'.format(cont3))
    print('Quantidade de notas de 1 real foram : {}'.format(cont4))
    print('Quantidade de moedas de 50 centavos foram : {}'.format(sc))
    print('Quantidade de moedas de 10 centavos foram : {}'.format(sc1))
    print('Quantidade de moedas de 5 centavos foram : {}'.format(sc2))
    print('Quantidade de moedas de 2 centavos foram : {}'.format(sc3))
    print('Quantidade de moedas de 1 centavos foram : {}'.format(sc4))
    