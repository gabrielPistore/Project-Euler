# Problem 2. Even Fibonacci Numbers


def generate_fibonacci_sequence(do_not_exceed):
    sequence = [1, 2]
    while (sequence[-2] + sequence[-1]) < do_not_exceed:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence


def sum_even_numbers(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))


print(sum_even_numbers(generate_fibonacci_sequence(4e6)))
