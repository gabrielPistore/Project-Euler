# Problem 006. Sum Square Difference


def sum_of_the_squares(num):
    sum_ = sum(n**2 for n in range(1, num + 1))
    return sum_


def square_of_the_sum(num):
    sum_ = sum((n for n in range(1, num + 1)))
    return sum_**2


print(square_of_the_sum(100) - sum_of_the_squares(100))
