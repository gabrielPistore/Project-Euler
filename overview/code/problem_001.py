def SumDivisibleBy(target, n):
    p = target / n
    return int(n * (p * (p + 1)) / 2)


print(SumDivisibleBy(999, 3) + SumDivisibleBy(999, 5) - SumDivisibleBy(999, 15))
