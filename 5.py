x=[1,2,5,6,7]
y=[2,3,7,9,10]
p=1
print('Suma componentelor de x =',sum(x))
print('Suma componenetelor de y =',sum(y))
print('Suma primelor trei componente =',sum(x[:3]))
for i in range(0,len(x)):
    p=p*x[i]
print('Produsul x=',p)
print('Valoarea absoluta=',y[2])
print('Suma primelor componente=',sum(x[:1]+y[:1]))