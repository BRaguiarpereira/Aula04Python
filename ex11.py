
n1 =  float(input( ' Deposito: ' ))
n2 =  float(input( ' Juros: ' ))
cont =  0
vj = 0
vs = 0
vf = 0
while cont!=23:
    vj = (n1*(n2/100))
    vs += vj
    cont =  cont + 1
    print('No mes {} voce teve um acrescimo de : {}'.format(cont,vs))
vf = vj + n1
print('Seu deposito ganhou um acrecimo de : {}'.format(vf))
