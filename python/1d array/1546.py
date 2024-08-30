# input
numberOfSubject = int(input())
scores = list(map(int, input().split()))

# Find Max score
maxScore = max(scores)

# Score transform
new_scores = [(score / maxScore) * 100 for score in scores]

# Calculate new average (transform score) / n
new_average = sum(new_scores) / numberOfSubject

print(new_average)
