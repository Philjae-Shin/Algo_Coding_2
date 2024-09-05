rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
for _ in range(20): # 단순히 반복만을 수행할 때 _ 사용
    subject, grade_input, rating_input = input().split()
    grade_input = float(grade_input)
    if grade_input != 'P':
        total += grade_input
        result += grade_input * grade[rating.index(rating_input)]

print('%.6f' % (result / total))
# 계산된 성적의 합계(result)를 총 학점(total)으로 나누어 **평균 성적(평점 평균)**을 계산
# %.6f는 소수점 6자리까지 출력하는 형식
