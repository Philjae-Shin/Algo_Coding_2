# cnt = int(input())
# numbers = list(map(int, input().split()))
# max = numbers[0]
# min = numbers[0]
#
# for i in numbers[:]:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
#
# print(min, max)

# No for loop
cnt = int(input())
numbers = list(map(int, input().split()))
print(min(numbers),max(numbers))