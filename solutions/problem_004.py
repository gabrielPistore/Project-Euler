# Problem 004. Largest Palindrome Product


def isPalindrome(palindrome):
    return str(palindrome) == str(palindrome[::-1])


palindromes = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        r = num1 * num2
        if isPalindrome(str(r)):
            palindromes.append(r)

print(max(palindromes))
