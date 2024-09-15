text = list(input())
cursor = len(text)

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        text.insert(cursor, command[1])
        cursor += 1
    elif command[0] == 'L':
        if cursor < 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor < len(text):
            cursor += 1
    else:
        if cursor > 0:
            text.remove(text[cursor-1])

print(''.join(text))
