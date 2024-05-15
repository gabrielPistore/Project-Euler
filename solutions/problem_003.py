# Problem 3. Largest Prime Factor


def largest_prime_factor(num):
    if num == 1:
        return 1

    factor = 2
    while factor <= num:
        if num % factor == 0:
            num /= factor
        else:
            factor += 1
    return factor


print(largest_prime_factor(600851475143))
