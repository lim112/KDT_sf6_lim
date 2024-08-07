#응용 학생 3명의 성적 통계
students = [
    {"name" : "이대한", 'kor' : 90, 'math' : 85},
    {"name" : "박민국", 'kor' : 80, 'math' : 75},
    {"name" : "임지능", 'kor' : 95, 'math' : 90}
]
'''print('♣ 개인별 성적표 ♣')
print("-" * 20)
print("이름  국어  수학")
print("-" * 20)
print(students[0]) #
print(students[1])
print(students[2])
print()

print('♣ 개인별 평균 성적표 ♣')
print("-" * 20)
print("이름  국어  수학  평균")
print("-" * 20)

for std in students:
    sum_score = std['kor'] + std['math']
    print(std["name"],std["kor"], " ",std["math"]," ", sum_score / 2)
    #list인 students 의 첫번재 행부터 students의
    # key에 매칭된 valuve를 찾아서 입력
    #이때 std는 students의 n번째 행을 불러온다
    sum_score = std['kor'] + std['math']
    print(sum_score)'''

#과목별 총점
math_sum_score = 0
kor_sum_score = 0
for std in students:
    math_sum_score += std['math']
    kor_sum_score += std['kor']

print("국어 총점 :", kor_sum_score) #국어 총점 : 265
print("수학 총점 :", math_sum_score) #수학 총점 : 250
print("국어 평균 :", kor_sum_score/len(students)) #국어 평균 : 88.33333333333333
print("수학 평균 :", math_sum_score/len(students)) #수학 평균 : 83.33333333333333


