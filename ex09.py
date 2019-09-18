n1 = int(input('n1:'))
n2 = int(input('n2:'))
cont = 0
total = n1
while total>= n2 :
    total=total-n2
    cont=cont+1
print('{}/{} = {} , resto {}'.format(n1,n2,cont,total) )

