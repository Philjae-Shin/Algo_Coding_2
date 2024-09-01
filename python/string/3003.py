require_pieces = [1, 1, 2, 2, 2, 8]

a = list(map(int, input().split()))

# make result list and append the value of (require_pieces) - (a) into result list
result = []
for i in range(6):
    result.append(require_pieces[i] - a[i])

# convert list to string
# func join: convert list to string
print(' '.join(map(str, result)))
