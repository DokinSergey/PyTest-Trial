import os
a = {'dev2300303':(r'e:\users\dev2300303', 'True')}
b = list(a.keys())[0]
c = a[b]
print(a)
print(b)
print(c[1])
c = a[list(a.keys())[0]]
print(c[1])
e = r'd:\direct\dev2300303'
print(os.path.splitext(e))
