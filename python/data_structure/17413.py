data = input()

stack = []
ans = ''
check = False # Check <>
for d in data:
    if d == '<':
        check = True
        while stack:
            ans += stack.pop() # Flip stack and append to ans
        ans += d # Add '<'

    elif d == '>':
        check = False
        ans += d # Add '>'

    elif d == ' ' and check == False:
        while stack:
            ans += stack.pop()
        ans += ' '

    else:
        stack.append(d)

# Handel remaining stack
while stack:
    ans += stack.pop()

print(ans)