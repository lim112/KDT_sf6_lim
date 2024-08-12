#학생 5명의 수학, 국어 총점과 평균
score = [
    [80,70], [70,95],[60, 90], [50, 75], [75,60]
]
total_p = []
#개인별 총점
personal = 0 #전역 변수로 할당하면 개인이든 과목이든 상관없이 다 더해져야하지 않나? 복습 필요
for i in range(len(score)):
    #personal = 0
    #for j in range(len((score[i])))
    personal = score[i][0] + score[i][1]
    total_p.append(personal)
    print("개인별 :", personal)

print(total_p) #[150, 165, 150, 125, 135]

math = 0
lang = 0
sum_subject = [0,0]
avg_subject = [0,0]
#반전체의 과목별 총점

for i in range(len(score)):
    sum_subject[0] += score[i][0]
    #복합대입 연산자를 사용할때는 전역변수 사용
    sum_subject[1] += score[i][1]

print(sum_subject) #[335, 390]

avg_subject[0] = sum_subject[0] / len(score[0])
avg_subject[1] = sum_subject[1] / len(score[0])

print(avg_subject[0]) #167.5
print(avg_subject[1]) #195.0

print("수학 :", sum_subject[0]) #수학 : 335
print("국어 :", sum_subject[1]) #국어 : 390
