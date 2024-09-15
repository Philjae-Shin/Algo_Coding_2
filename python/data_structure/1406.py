# Time Complexity = O(n)

# text = list(input())
# cursor = len(text)
#
# for _ in range(int(input())):
#     command = list(input().split())
#     if command[0] == 'P':
#         text.insert(cursor, command[1])
#         cursor += 1
#     elif command[0] == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif command[0] == 'D':
#         if cursor < len(text):
#             cursor += 1
#     else:
#         if cursor > 0:
#             text.remove(text[cursor-1])
#
# print(''.join(text))

# Time Complexity = O(1)

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))
