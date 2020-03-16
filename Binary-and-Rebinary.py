# Two little function for convert numeral system.

def binary(x):
    if x == 0:
        return str(0)

    otv = ''
    while x > 1:
        otv += str(x % 2)
        x = x // 2
    otv += '1'
    return (otv[::-1])


def rebinary(x):
    st = 0
    otv = 0
    while len(x) > 0:
        if int(x[len(x) - 1]) == 1:
            otv += 2 ** st
            st += 1
        x = x[0:len(x) - 1]
    return otv


print(rebinary('101'))
print(binary(5))
