# Problem 010. Summation of Primes

import math


def isPrime(n):
    if n == 1:
        return False
    elif n < 4:  # 2 and 3 are prime
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:  # we have already excluded 4,6 and 8
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(
            math.sqrt(n)
        )  #  sqrt(n) rounded to the greatest integer r so that r*r<=n
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f + 2) == 0:
                return False
            f += 6
        return True


def summation_of_primes(threshold):
    summation = 2 + 3
    n = 5
    while n < threshold:
        if isPrime(n):
            summation += n
        if isPrime(n + 2):
            summation += n + 2
        n += 6
    return summation


print(summation_of_primes(2e6))
