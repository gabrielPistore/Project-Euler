def prime_factorization(num):
    factors = []

    if num == 1:
        return factors

    factor = 2
    while factor <= num:
        if num % factor == 0:
            factors.append(factor)
            num /= factor
        else:
            factor += 1
    return factors


print(prime_factorization(2520))
