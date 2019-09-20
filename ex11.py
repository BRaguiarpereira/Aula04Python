n1 =  float(input( ' Deposito: ' ))
n2 =  float(input( ' Juros: ' ))
vj = 0
vs = 0
vf = 0
while cont!=24:
    vj = (n1*(n2/100))
    vs += vj
    cont =  cont + 1
    vf = vs + n1
    print('No mes {} voce teve um acrescimo de : {}'.format(cont,vs))
print('Seu deposito ficou com o saldo de : {}'.format(vf))
