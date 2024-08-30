n, m = map(int, input().split())

box = [0] * n

for a in range(m):
    i, j, k = map(int, input().split())
    for i in range(i, j+1):
        box[i-1] = k
for i in range(n):
    box = map(str, box)
print(" ".join(box))