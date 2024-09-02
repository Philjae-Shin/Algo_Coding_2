n = int(input())

# upper pyramid
for i in range(1, n):
    print(' ' * (n-i) + '*' * (2 * i - 1))

# lower pyramid
for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * (2 * i - 1))
