alfa = {'0': '00001', '1': '00010', '2': '00100', '3': '01000', '4': '10000', '5': '00101', '6': '01010', '7': '10100',
        '8': '01101', '9': '11010', '10': '10001', '11': '00111', '12': '01110', '13': '11100', '14': '11101',
        '15': '11111', '16': '11011', '17': '10011', '18': '00011', '19': '00110', '20': '01100', '21': '11000',
        '22': '10101', '23': '01111', '24': '11110', '25': '11001', '26': '10111', '27': '01011', '28': '10110',
        '29': '01001', '30': '10010', '31': '00000'}


# alphabet = list('abcdefghijklmnopqrstuvwxyzаесорх')


def ikey(value):
    global alfa
    for key, a in alfa.items():
        if a == value:
            return key


action = int(input("affine cipher\nPress 1 if you want encrypt or 2 if you want decipher\n"))
select = int(input("select your alphabet\nEnglish - 1\nRussian - 2\n"))
if select == 1:
    alphabet = list('abcdefghijklmnopqrstuvwxyzаесорх')
elif select == 2:
    alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
else:
    print('Invalid value')
if action == 1:
    text = str(input('Your word\n'))
    alpha = str(input('your alpha\n'))
    if alpha == '00000':
        print('Invalid value')
    else:
        betta = str(input('Your betta\n'))
        plain_text = ''
        for i in text:
            i = i.lower()
            if i == "":
                plain_text += ''
            else:
                plain_text += i.lower()
        encode_text = ''
        for i in plain_text:
            if i == " ":
                encode_text += ' '
                continue
            ind_alpha = int(ikey(alpha))
            ind_letter_pl = alphabet.index(i)
            ind_letter_aapl = str((ind_alpha + ind_letter_pl) % 32)
            bin_seq = alfa[ind_letter_aapl]
            result = ''
            for i in range(len(bin_seq)):
                result += str((int(bin_seq[i]) + int(betta[i])) % 2)
            bin_seq_final = result
            ind_final = int(ikey(bin_seq_final))
            encode_text += alphabet[ind_final]
        print(encode_text)
if action == 2:
    encode_text = str(input('Your word\n'))
    alpha = str(input('Your alpha\n'))
    if alpha == '00000':
        print('Invalid value')
    else:
        betta = str(input('Your betta\n'))
        decode_text = ''
        alpha_rev = 32 - int(ikey(alpha))
        for i in encode_text:
            if i == " ":
                decode_text += ' '
                continue
            val = alfa[str(alphabet.index(i))]
            result = ''
            for i in range(len(val)):
                result += str((int(val[i]) - int(betta[i])) % 2)
            bin_req = result
            key1 = int(ikey(bin_req))
            decode_text += alphabet[(key1 + alpha_rev) % 32]
        print(decode_text)
