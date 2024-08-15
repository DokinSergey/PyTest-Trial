di = {'a':['10',False],'b':['11',False],'c':['12',False],'d':['13',False],'e':['14',False],'f':['15',False]}
for n,idi in enumerate(di.items()):
    print(n,idi[0],idi[1][0],idi[1][1])
ifl = 'ibases_dev24001-unf-bnmiyqs.v8i'[7:-4]
print(ifl)
Password = ('1','2','4','а')
print(any(chk in Password for chk in ('A','a','А','а')))