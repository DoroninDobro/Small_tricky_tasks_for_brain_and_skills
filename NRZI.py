'''Interesting task and I add more hard reverse function

NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. Обладает двумя уровнями сигнала и используется для передачи битовых последовательностей, содержащих только 0 и 1. NRZI применяется, например, в оптических кабелях, где устойчиво распознаются только два состояния сигнала — свет и темнота.

Принцип кодирования При передаче логического нуля на вход кодирующего устройства передается потенциал, установленный на предыдущем такте (то есть состояние потенциала не меняется), а при передаче логической единицы потенциал инвертируется на противоположный.'''

def decode(x):
    z = ''
    i = 0
    while i < len(x):
        if x[i] == '|':
            z += '1'
            i += 2
        else:
            z += '0'
            i += 1
    return z
    
def write(up):
    if up == False:
        return '_'
    else: 
        return '¯'
        
def turn_write(up):
    if up == True:
        return False
    else: 
        return True
    
def code(x):
    up = False
    z = ''
    i = 0
    while i < len(x):
        if x[i] == '0':
            z += write(up)
            i += 1
        else: 
            up = turn_write(up)
            z += '|' + write(up)
            i += 1
    return z
