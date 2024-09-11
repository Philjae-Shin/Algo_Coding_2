import sys

# test_case
t = int(input())

for _ in range(t):
    sentence = sys.stdin.readline().rstrip()
    words = list(sentence.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = ' '.join(reverse_words)
    print(answer)
