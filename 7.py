o=[8,3,4,2,2,16,9,4,0,11,13,14,21,6,17,15,12,5,7,8,21,10,13]
t=[6,2,2,7,5,12,8,7,1,0,9,21,21,10,17,7,4,12,20,8,2,2,1,19]
print('t medie=', round(sum(t)/24,1))
print('t maxima=',max(t))
print('t minima=',min(t))
print('ora la care s-a inregistrat temperatura maxima: ',o[t.index(max(t))])
print('ora la care s-a inregistrat temperatura minima: ',o[t.index(min(t))])