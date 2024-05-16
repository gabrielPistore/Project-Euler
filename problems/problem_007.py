# Problem 007. 10001st Prime


def isPrime(num):
    if num == 1:
        return False

    factor = 2
    while factor < num:
        if num % factor == 0:
            return False
        factor += 1

    return True


def prime(n):
    c = 0
    num = 2
    while True:
        if isPrime(num):
            c += 1
        if c == n:
            return num
        num += 1


print(prime(10001))
