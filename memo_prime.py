'''A prime number is an integer greater than 1 that is only evenly divisible by itself and 1.

Write your own Primes class with class method Primes.first(n) that returns an array of the first n prime numbers.'''


from math import sqrt

class Primes:
    
    lst = [2]
    i = 3

    def first(n):
        if n < len(Primes.lst):
            return Primes.lst[:n]
        while len(Primes.lst) < n:
            if (Primes.i > 10) and (Primes.i%10==5):
                Primes.i += 2
                continue
            for j in Primes.lst:
                if j > int((sqrt(Primes.i)) + 1):
                    Primes.lst.append(Primes.i)
                    break
                if (Primes.i % j == 0):
                    break
            else:
                Primes.lst.append(Primes.i)
            Primes.i +=2
        return Primes.lst
