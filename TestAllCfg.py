V8iName = '\\\moscow\\ibases\\dev23007\\ibases_dev22001-acc-fufcy.v8i'
#------------------------------------------------------------------------------------------------------------------
# IbaseAll = '\\\moscow\\ibases\\OMC_ibases\\1cestart.cfg', encoding='utf_8', encoding='utf_8'
IbaseAll = '\\\moscow\\ibases\\OMC_Demo\\1cestart.cfg'
IBlist = []
print(V8iName, len(V8iName))
# with open(IbaseAll, mode ='r', encoding='utf_16_le') as Allcfg:
    # for line in Allcfg.readlines():
        # sline =line.split('=')

        # if (sline[0] == 'CommonInfoBases'):
            # print(len(sline[-1]), sline[-1], end='')
            
            # if (sline[-1].strip() == V8iName.strip()):
                # print('tfghjkll')
                # break
    # else:
        # print(f'CommonInfoBases={V8iName}')
        # with open(IbaseAll, mode ='a', encoding='utf_16_le') as Allcfg:
            # print(f'CommonInfoBases={V8iName}',file=Allcfg)
# input('Нажмите "Enter" для закрытия окна') 

with open(IbaseAll, mode ='r', encoding='utf_16_le') as Allcfg:
    for line in Allcfg.readlines():
        if line.startswith('CommonInfoBases'):
            print(len(line), line, end='')
            if line.strip().endswith(V8iName.strip()):
                print('Уже добавлено')
                break
    else:
        print(f'CommonInfoBases={V8iName}')
        with open(IbaseAll, mode ='a', encoding='utf_16_le') as Allcfg:
            print(f'CommonInfoBases={V8iName}',file=Allcfg)