zi = ['L', 'Ma', 'Mi', 'J', 'Vi', 'S', 'D']
v = [2489,905,1789,1994,1129,855,983] 
print('Venit saptamanal:', sum(v))
print('Media venitului zilnic:', sum(v)/7)
print('Ziua cu cel mai mare venit:',zi[v.index(max(v))])
print('Ziua cu cel mai mic venit:',zi[v.index(min(v))])