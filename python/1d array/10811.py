# input
n, m = map(int, input().split())

# make list of initial basket
baskets = list(range(1, n+1))

# repeat m times of job
for _ in range(m):
    i, j = map(int, input().split())
    # 리스트의 슬라이싱과 역순으로 바꾸는 기능을 이용하여 처리
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(" ".join(map(str, baskets)))
