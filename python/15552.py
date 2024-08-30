import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split()) # Can use input(), problem: runtime
    print(a + b)