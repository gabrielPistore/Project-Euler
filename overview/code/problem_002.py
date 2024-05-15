limit = 4e6
sum_ = 0
a = 1
b = 1
c = a + b
while c < limit:
    sum_ = sum_ + c

    a = b + c
    b = c + a
    c = a + b
print(sum_)
