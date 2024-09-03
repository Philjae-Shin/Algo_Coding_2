from collections import Counter # Counter는 이터러블(리스트, 문자열 등)의 각 요소가 몇 번씩 등장했는지 세어주는 클래스

# strip(): 문자열의 앞뒤에 있는 공백을 제거
# upper(): 문자열을 모두 대문자로 변환
word = input().strip().upper()

counter = Counter(word)
max_count = max(counter.values()) # counter.values()는 counter 딕셔너리의 값(즉, 각 알파벳의 빈도수)을 반환
most_common = [key for key, value in counter.items() if value == max_count]
# list comprehension 안 쓰고 표현
# most_common = []
# for key, value in counter.items():
    # if value == max_count:
        # most_common.append(key)

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])
