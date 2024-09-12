# VPS

t = int(input())

for i in range(t):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # if there is no PS in stack
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됐을경우 수행한다.
        if not stack:
            print("Yes")
        else:
            print("NO")

