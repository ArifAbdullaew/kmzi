alfa = {'0': '00001', '1': '00010', '2': '00100', '3': '01000', '4': '10000', '5': '00101', '6': '01010', '7': '10100',
        '8': '01101', '9': '11010', '10': '10001', '11': '00111', '12': '01110', '13': '11100', '14': '11101',
        '15': '11111', '16': '11011', '17': '10011', '18': '00011', '19': '00110', '20': '01100', '21': '11000',
        '22': '10101', '23': '01111', '24': '11110', '25': '11001', '26': '10111', '27': '01011', '28': '10110',
        '29': '01001', '30': '10010', '31': '00000'}
#alphabet = list('abcdefghijklmnopqrstuvwxyzаесорх')


def summation(first, second):
    result = ''
    for i in range(len(first)):
        result += str((int(first[i]) + int(second[i])) % 2)

    return result


def key(value):
    global alfa
    for key, a in alfa.items():
        if a == value:
            return key


action = int(input("affine recurrent cipher\nPress 1 if you want encrypt or 2 if you want decipher\n"))
select = int(input("select your alphabet\nEnglish - 1\nRussian - 2\n"))
if select == 1:
    alphabet = list('abcdefghijklmnopqrstuvwxyzаесорх')
elif select == 2:
    alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
else:
    print('Invalid value')
if action == 1:
    plain_text = str(input('Your word\n'))
    plain_text = plain_text.lower()
    firstalpha = str(input('Your first alpha\n'))
    firstbetta = str(input('Your first betta\n'))
    secondalpha = str(input('Your second alpha\n'))
    secondbetta = str(input('Your second betta\n'))
    if (firstalpha == '00000') or (secondalpha == '00000'):
        print('Invalid value')
    else:
        encode_text = ''
        n = 1
        for i in plain_text:
            if n == 1:
                if i == " ":
                    encode_text += ' '
                else:
                    alpha = firstalpha
                    betta = firstbetta
                    ind_alpha = int(key(alpha))
                    ind_letter_pl = alphabet.index(i)
                    ind_letter_aapl = str((ind_alpha + ind_letter_pl) % 32)
                    bin_seq = alfa[ind_letter_aapl]
                    result = ''
                    for i in range(len(bin_seq)):
                        result += str((int(bin_seq[i]) + int(betta[i])) % 2)
                    bin_seq_final = result
                    ind_final = int(key(bin_seq_final))
                    encode_text += alphabet[ind_final]
                    n += 1
            elif n == 2:
                if i == " ":
                    encode_text += ' '
                else:
                    alpha = secondalpha
                    betta = secondbetta
                    ind_alpha = int(key(alpha))
                    ind_letter_pl = alphabet.index(i)
                    ind_letter_aapl = str((ind_alpha + ind_letter_pl) % 32)
                    bin_seq = alfa[ind_letter_aapl]
                    result = ''
                    for i in range(len(bin_seq)):
                        result += str((int(bin_seq[i]) + int(betta[i])) % 2)
                    bin_seq_final = result
                    ind_final = int(key(bin_seq_final))
                    encode_text += alphabet[ind_final]
                    n += 1
            else:
                if i == " ":
                    encode_text += ' '
                else:
                    key1 = int(key(firstalpha))
                    key2 = int(key(secondalpha))
                    alpha_ = str((key1 + key2) % 32)
                    alpha = alfa[alpha_]
                    betta = summation(firstbetta, secondbetta)
                    ind_alpha = int(key(alpha))
                    ind_letter_pl = alphabet.index(i)
                    ind_letter_aapl = str((ind_alpha + ind_letter_pl) % 32)
                    bin_seq = alfa[ind_letter_aapl]
                    result = ''
                    for i in range(len(bin_seq)):
                        result += str((int(bin_seq[i]) + int(betta[i])) % 2)
                    bin_seq_final = result
                    ind_final = int(key(bin_seq_final))
                    encode_text += alphabet[ind_final]
                    firstalpha = secondalpha
                    secondalpha = alpha
                    firstbetta = secondbetta
                    secondbetta = betta
        print(encode_text)

if action == 2:
    plain_text = str(input('Your word\n'))
    firstalpha = str(input('Your first alpha\n'))
    firstbetta = str(input('Your first betta\n'))
    secondalpha = str(input('Your second alpha\n'))
    secondbetta = str(input('Your second betta\n'))
    if (firstalpha == '00000') or (secondalpha == '00000'):
        print('Invalid value')
    else:
        decode_text = ''
        firstalpha_reversed = 32 - int(key(firstalpha))
        secondalpha_reversed = 32 - int(key(secondalpha))
        n = 1
        a = 0
        for i in encode_text:
            if n == 1:
                if i == ' ':
                    decode_text += ' '
                else:
                    alpha = firstalpha_reversed
                    betta = firstbetta
                    val = alfa[str(alphabet.index(i))]
                    result = ''
                    for i in range(len(val)):
                        result += str((int(val[i]) - int(betta[i])) % 2)
                    bin_req = result
                    key1 = int(key(bin_req))
                    decode_text += alphabet[(key1 + alpha) % 32]
                    n += 1
            elif n == 2:
                if i == ' ':
                    decode_text += ' '
                else:
                    alpha = secondalpha_reversed
                    betta = secondbetta
                    val = alfa[str(alphabet.index(i))]
                    result = ''
                    for i in range(len(val)):
                        result += str((int(val[i]) - int(betta[i])) % 2)
                    bin_req = result
                    key1 = int(key(bin_req))
                    decode_text += alphabet[(key1 + alpha) % 32]
                    n += 1
            else:
                alpha_reversed = (firstalpha_reversed + secondalpha_reversed) % 32
                result = ''
                for i in range(len(firstbetta)):
                    result += str((int(firstbetta[i]) + int(secondbetta[i])) % 2)
                betta = result
                val = alfa[str(alphabet.index(i))]
                result = ''
                for i in range(len(val)):
                    result += str((int(val[i]) - int(betta[i])) % 2)
                bin_req = result
                key1 = int(key(bin_req))
                decode_text += alphabet[(key1 + alpha_reversed) % 32]
                firstalpha_reversed = secondalpha_reversed
                secondalpha_reversed = alpha_reversed
                firstbetta = secondbetta
                secondbetta = betta
        print(decode_text)
