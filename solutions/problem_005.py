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


def count_appearance(lst):
    count = {}
    for element in lst:
        if count.get(element):
            count[element] += 1
        else:
            count[element] = 1
    return count


smallest_multiple_factors = {}  # type: ignore
for num in range(2, 21):
    factors = prime_factorization(num)
    count = count_appearance(factors)  # type: ignore
    for key, value in count.items():
        if smallest_multiple_factors.get(key, 0) < count[key]:
            smallest_multiple_factors[key] = count[key]

smallest_multiple = 1
for num, quantity in smallest_multiple_factors.items():
    smallest_multiple *= num**quantity
print(smallest_multiple)
