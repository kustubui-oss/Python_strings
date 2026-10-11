# задание 1.1
stroka = input("введите текст:")

spisok = []
znaki = '.,!?:;-()"\'+_@#%*'
sl = ''

for st in stroka:
    if st != ' ' and st not in znaki:
        sl += st
    elif st == ' ' and sl != '':
        spisok.append(sl)
        sl = ''
    elif st in znaki:
        spisok.append(sl)
        spisok.append(st)
        sl = ''


index_znaki = []
znaki_new = []
id_slova = []
slova = []

for i in range(len(spisok)):
    if spisok[i] in znaki:
        index_znaki.append(i)
        znaki_new.append(spisok[i])
    else:
        id_slova.append(i)
        slova.append(spisok[i])

result = [''] * len(spisok)
new_slov = []

for i in range(len(id_slova) - 1, -1, -1):
    new_slov.append(slova[i])

for i in range(len(index_znaki)):
    result[index_znaki[i]] = znaki_new[i]

for i in range(len(id_slova)):
    result[id_slova[i]] = new_slov[i]

for i in result:
    print(i, end = ' ')
