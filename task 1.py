import csv
with open('C:\\Users\\Kids01\\Desktop\\Вариант 30\\count_company.txt') as file:
    i=[]
    for x in file:
        i.append(x)
    if i.index('Netbook\n')< i.index('Notebook\n') and i.index('Ultrabook\n')<i.index('Netbook\n'):
        k=i[i.index('Ultrabook\n'):i.index('Netbook\n')]
    elif i.index('Netbook\n')> i.index('Notebook\n') and i.index('Ultrabook\n')<i.index('Notebook\n'):
        k=i[i.index('Ultrabook\n'):i.index('Notebook\n')]
    elif i.index('Netbook\n')< i.index('Notebook\n') and i.index('Ultrabook\n')>i.index('Notebook\n') and i.index('Ultrabook\n')<i.index('Netbook\n'):
        k=i[i.index('Ultrabook\n'):i.index('Netbook\n')]
    elif i.index('Netbook\n')< i.index('Notebook\n') and i.index('Ultrabook\n')>i.index('Netbook\n') and i.index('Ultrabook\n')<i.index('Notebook\n'):
        k=i[i.index('Ultrabook\n'):i.index('Notebook\n')]
    else:
        k=i[i.index('Ultrabook\n')::]
    for z in k:
        print(z)

