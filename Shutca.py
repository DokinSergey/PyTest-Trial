x=0
y=0
while True:
    x += 1
    y += 1
    if x is y:
        print( f'{x = }:{id(x) =}:{id(y) =}: equal!')
    else:
        print( f'{x = }:{id(x) =}:{id(y) =}: not equal!')
        break

    
