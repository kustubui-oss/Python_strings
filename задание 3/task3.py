# задание 3
text = input("введите текст:")

text_low = text.lower()
znaki = '.,?!#@№()-_=+\"%^* '
sp_slov = []
sl = ''

for i in text_low:
    if i not in znaki:
       sl += i

    elif i in znaki and sl != '':
        sp_slov.append(sl)
        sl = ''

if sl != '':
    sp_slov.append(sl)

counter = []

for word in sp_slov:
    found = False

    for item in counter:
        if item[0] == word:
            item[1] += 1
            found = True
            break

    if found == False:
        counter.append([word, 1])

for i in range(len(counter)):
    for j in range(i + 1):
        if counter[j][1] < counter[i][1]:
            m = counter[i]
            counter[i] = counter[j]
            counter[j] = m

print('топ-5 частых слов в тексте')

limit = 5

if len(counter) < limit:
    limit = len(counter)

for i in range(limit):
    word = counter[i][0]
    count = counter[i][1]
    print(word, ':', count)


