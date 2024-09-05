a, b = [], []

n, m = map(int, input().split())

#  A, B 에 행렬의 원소를 입력 받는다
for row in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for row in range(n):
    row = list(map(int, input().split()))
    b.append(row)

# 행렬 A, B 를 더한 행렬을 출력한다
for row in range(n):
    for col in range(m):
        # 반복문을 통해 행렬 A, B 의 동일 행, 동일 열에 위치한 원소를 더한 값을 출력하고, end = ' ' 를 통해 띄어쓰기로 열을 구분하여 출력한다.
        print(a[row][col] + b[row][col], end=' ')
    # 하나의 열을 출력한다음, 다음 행으로 넘어가기 전에 print() 를 통해 줄바꿈을 해주어 행을 구분한다.
    print()
