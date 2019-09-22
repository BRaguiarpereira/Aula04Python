n1 = float(input('Digite valor da divida:'))
n2 = float(input('Digite valor do juros:'))
n3 = float(input('Valor mensal pago :'))
cont = 0
vj = 0
vs = 0
vf = 0
vd = n1
while n1!=0:
    n1 = n1 - n3
    vj = (n1*(n2/100))
    vs += vj
    cont = cont +1
    print('Sua divida no mes {} é : {}'.format(cont,n1))
    print('Com juros de : {}'.format(vj))
vf = vs + vd
print('O juros total foi de : {} reais'.format(vs)) 
print('O valor final da sua divida com juros é de : {} reais'.format(vf))  
print('Sua divida será paga em {} meses '.format(cont))
