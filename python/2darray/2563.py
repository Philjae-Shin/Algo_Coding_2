# Can express, ary = [[0]*11 for i in range(10)] : row = 11, col = 10
ary = [[0 for _ in range(101)]for _ in range(101)] # init 2d array [0, 0, 0], row: 101 col:101
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))

    for row in range(x, x+10):
        for col in range(y, y+10):
            ary[row][col] = 1

result = 0

for i in ary:
    result += i.count(1)
print(result)

