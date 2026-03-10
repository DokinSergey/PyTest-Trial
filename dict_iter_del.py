a = {'a':'1','b':'2','c':'3','d':'4','e':'5'}
b = []
for ai in list(a.keys()):
    b.append((ai,a.get(ai,'')))
print(f'{a = }')
print(f'{b = }')
