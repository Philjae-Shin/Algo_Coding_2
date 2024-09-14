count = 1
temp = True
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

    # num == stack[-1], remove stack[-1] element
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if not temp:
    print("NO")
else:
    for i in op:
        print(i)
