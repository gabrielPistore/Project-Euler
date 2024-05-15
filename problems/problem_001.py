# Problem 1. Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_all_the_multiples(number):
    sum_ = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i
    return sum_


print(sum_of_all_the_multiples(1000))
