
n2 =  float(input( ' Juros: ' ))
cont =  0
vj = 0
vj2 = vj
vs = 0
vf = 0
while cont!=24:
    n1 =  float(input( ' Deposito: ' ))
    vj = (n1*(n2/100))+n1
    vj2 = (vj*(n2/100))+n1
    vs += vj
    cont =  cont + 1
    vf = vs + n1
    print('No mes {} voce teve um acrescimo de : {}'.format(cont,vs))
print('Seu deposito ficou com o saldo de : {}'.format(vf))
