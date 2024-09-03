word = input()

# [:-1] 마지막 원소를 제외하고 나머지를 순서대로 반환
# [::-1] 원래 순서와 반대로 뒤집어서 모든 원소를 반환
if word == word[::-1]:
    print(1)
else:
    print(0)
