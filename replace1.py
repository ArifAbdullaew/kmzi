print('Default Replace Cipher')
choice = int(input('Press 1 if you want encrypt or 2 if you want decipher\n'))
if choice == 1:
    language = int(input('Press your alphabet for the corresponding number\n English - 1\n Russian - 2\n Another - 3\n'))
    if language == 1:
        yourdict = list('abcdefghijklmnopqrstuvwxyz')
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        encode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                encode += ' '
                continue
            determinant = int(yourdict.index(i))
            encode += type[determinant]
        print(encode)
    if language == 2:
        yourdict = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        encode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                encode += ' '
                continue
            determinant = int(yourdict.index(i))
            encode += type[determinant]
        print(encode)
    if language == 3:
        yourdict = input('Alphabet of your language\n')
        language = type(yourdict)
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        encode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                encode += ' '
                continue
            determinant = int(yourdict.index(i))
            encode += type[determinant]
        print(encode)
if choice == 2:
    language = int(
        input('Press your alphabet for the corresponding number\n English - 1\n Russian - 2\n Another - 3\n'))
    if language == 1:
        yourdict = list('abcdefghijklmnopqrstuvwxyz')
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        decode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                decode += ' '
                continue
            determinant = int(type.index(i))
            decode += yourdict[determinant]
        print(decode)
    if language == 2:
        yourdict = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        decode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                decode += ' '
                continue
            determinant = int(type.index(i))
            decode += yourdict[determinant]
        print(decode)
    if language == 3:
        yourdict = input('Alphabet of your language\n')
        language = type(yourdict)
        message = input('Your word\n ')
        message = message.lower()
        newalphabet = input('Your secret alphabet\n ')
        decode = ''
        type = (newalphabet)
        for i in message:
            if i == ' ':
                decode += ' '
                continue
            determinant = int(type.index(i))
            decode += yourdict[determinant]
        print(decode)