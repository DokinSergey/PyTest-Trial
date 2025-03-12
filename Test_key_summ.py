
test_dict = {'a':1}

while (inkeys := input('key,value :-> ')):
    key,value = inkeys.split(',')
    if (oldvalue := test_dict.get(key)) is None:
        test_dict.setdefault(key,int(value))
    else: test_dict[key] = oldvalue + int(value)
    print(test_dict)
input('Exit :-> ')
