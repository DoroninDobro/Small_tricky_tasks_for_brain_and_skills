import itertools

def encrypt(text, n):
    final_text = text
    while n > 0:
        text = final_text
        text1 = []
        text = list(text)
        c = 0
        while c < len(text):
            text1.append(text.pop(c))
            c += 1
        final_text = ''.join(text + text1)
        n -= 1
    return final_text


def decrypt(en_text, n):
    finish = en_text
    while n > 0:
        en_text = finish
        pos = len(en_text)//2
        start = list(en_text[pos:])
        add = list(en_text[:pos])
        finish = ''
        for i in itertools.zip_longest(start, add):
            if i[1] == None:
                finish += str(i)[2]
                break
            print(i[0])
            z = '\\'
            if str(i[0]) == z:
                finish += str(i)[2] + str(i)[8]
            else:
                finish += str(i)[2] + str(i)[7]
        n -= 1
    return finish


'''For building the encrypted string:
Take every 2nd char from the string, then the other chars, 
that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.'''