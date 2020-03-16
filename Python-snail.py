'''My first complete 4kyu task =))

Snail Sort Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3], [4,5,6], [7,8,9]] snail(array) #=> [1,2,3,6,9,8,7,4,5] For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3], [8,9,4], [7,6,5]] snail(array) #=> [1,2,3,4,5,6,7,8,9]'''

def snail(x):
    z = []
    while len(x) > 0:
        #right
        while x[0] != []:
            z.append(x[0][0])
            del x[0][0]
        del x[0]
        if len(x) == 0: break
        #down
        for i in range(len(x)):
            z.append(x[i][-1])
            del x[i][-1]
        if len(x) == 0: break
        #left
        while x[-1] != []:
            z.append(x[-1][-1])
            del x[-1][-1]
        del x[-1]
        if len(x) == 0: break
        #up
        for j in range(len(x)-1, 0, -1):
            z.append(x[j][0])
            del x[j][0]
        if len(x) == 0: break
    return z
