import sys

# test_case
t = int(input())

for _ in range(t):
    word_input = sys.stdin.readline().rstrip()
    words = list(word_input.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = ' '.join(reverse_words)
    print(answer)
