a, b = input().split()

# Reverse a, b
reversed_a = a[::-1] # reverse and make new list
reversed_b = b[::-1]

# print max value comparing reversed_a and reversed_b
print(max(reversed_a, reversed_b))
