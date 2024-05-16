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
    if n % 3 == 0:
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


limit = 10001
count = 1
candidate = 1
while True:
    candidate += 2
    if isPrime(candidate):
        count += 1
    if count == limit:
        break

print(candidate)
