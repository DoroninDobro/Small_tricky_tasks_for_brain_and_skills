def encrypt(text, key):
    if key == 0:
        return text
    key = list(str(key))
    for i in range(len(key)):
        key[i] = key[i] * 2
    key = ''.join(key)
    key = list(key)
    list_ = []
    uprow = list('qwertyuiop')
    list_.append(uprow)
    uprowU = list('QWERTYUIOP')
    list_.append(uprowU)
    midrow = list('asdfghjkl')
    list_.append(midrow)
    midrowU = list('ASDFGHJKL')
    list_.append(midrowU)
    downrow = list('zxcvbnm,.')
    list_.append(downrow)
    downrowU = list('ZXCVBNM<>')
    list_.append(downrowU)
    text = list(text)
    for i in range(len(text)):
        ff = 0
        for z in range(len(list_)):
            if text[i] in list_[z]:
                ff = 1
                break
            z += 1
        if ff == 0:
            continue
        local_list = ''.join(list_[z])
        u = local_list.find(text[i])
        fp = u + int(key[z])
        if fp >= len(local_list): 
            fp = fp - len(local_list)
        text[i] = list_[z][fp]
    text = ''.join(text)
    return text
    
    
def decrypt(text, key):
    if key == 0:
        return text
    key = list(str(key))
    for i in range(len(key)):
        key[i] = key[i] * 2
    key = ''.join(key)
    key = list(key)
    list_ = []
    uprow = list('qwertyuiop')
    list_.append(uprow)
    uprowU = list('QWERTYUIOP')
    list_.append(uprowU)
    midrow = list('asdfghjkl')
    list_.append(midrow)
    midrowU = list('ASDFGHJKL')
    list_.append(midrowU)
    downrow = list('zxcvbnm,.')
    list_.append(downrow)
    downrowU = list('ZXCVBNM<>')
    list_.append(downrowU)
    text = list(text)
    for i in range(len(text)):
        ff = 0
        for z in range(len(list_)):
            if text[i] in list_[z]:
                ff = 1
                break
            z += 1
        if ff == 0:
            continue
        local_list = ''.join(list_[z])
        u = local_list.find(text[i])
        fp = u - int(key[z])
        if fp >= len(local_list): 
            fp = fp + len(local_list)
        text[i] = list_[z][fp]
    text = ''.join(text)
    return text


''' You have to write two methods to encrypt and decrypt strings. Both methods have two parameters:

1. The string to encrypt/decrypt
2. The Qwerty-Encryption-Key (000-999) 
The rules are very easy:

The crypting-regions are these 3 lines from your keyboard:
1. "qwertyuiop"
2. "asdfghjkl"
3. "zxcvbnm,."

If a char of the string is not in any of these regions, take the char direct in the output.
If a char of the string is in one of these regions: Move it by the part of the key in the 
region and take this char at the position from the region. 
If the movement is over the length of the region, continue at the beginning.
The encrypted char must have the same case like the decrypted char! 
So for upperCase-chars the regions are the same, but with pressed "SHIFT"!

The Encryption-Key is an integer number from 000 to 999. E.g.: 127

The first digit of the key (e.g. 1) is the movement for the first line.
The second digit of the key (e.g. 2) is the movement for the second line.
The third digit of the key (e.g. 7) is the movement for the third line.

(Consider that the key is an integer! When you got a 0 this would mean 000. A 1 would mean 001. And so on.)
You do not need to do any prechecks. The strings will always be not null and will always have a length > 0. You do not have to throw any exceptions.
'''