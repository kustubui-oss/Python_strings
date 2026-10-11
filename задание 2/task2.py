# задание 2
text = input("введите текс на английском языке(не забудьте точку на конце):")

low_alf = 'abcdefghijklmnopqrstuvwxyz'
up_alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sign = ':;!?\'*_-=+^%#№@, '
sp = []
sl = ''
ma = 0

for letter in text:
    if letter not in sign and letter != '.':
        sl += letter

    elif letter in sign and sl != '':
        sp.append(sl)
        sp.append(letter)

        if len(sl) > ma:
            ma = len(sl)

        sl = ''

    elif letter == '.':
        sp.append(sl)
        sp.append(letter)

        if len(sl) > ma:
            ma = len(sl)

        break

res = ''

for letter in range(len(text)):
    if text[letter] in low_alf:

        for lf in range(len(low_alf)):
            if low_alf[lf] == text[letter]:
                new_letter = (lf + ma) % 26
                res += low_alf[new_letter]

    elif text[letter] in up_alf:

        for lf in range(len(up_alf)):
            if up_alf[lf] == text[letter]:
                new_letter = (lf + ma) % 26
                res += up_alf[new_letter]

    elif text[letter] not in low_alf and text[letter] not in up_alf and text[letter] != '.':
        res += text[letter]

    elif text[letter] == '.':
        res += '.'
        break

print(res)


