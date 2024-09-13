count = 1
temp = 0
stack = []
op = []

n = int(input())
for i in range(n):
    num = int(input())
    # put number in stack least than num
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
