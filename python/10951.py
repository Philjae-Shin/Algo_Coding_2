# while 1:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break

# Runtime better code
import sys

for i in sys.stdin:
    A, B = map(int, i.split())
    print(A+B)