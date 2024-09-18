n, k = map(int, input().split())
# init first circle

arr = []
for i in range(1, n + 1):
    arr.append(i)
    # arr = [i for i in range(1, n + 1)]

answer = [] # 제거된 사람들을 넣을 배열
num = 0 # 제거될 사람의 인덱스 번호

# Elimination process
for t in range(n):
    num += k - 1
    if num >= len(arr):
        # Use modulo to adjust len(arr)
        num = num % len(arr)

    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')
