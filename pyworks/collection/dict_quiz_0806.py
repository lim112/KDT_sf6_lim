#실습1
#1,2
scores = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
#3
scores["David"] = 80
#4
scores["Alice"] = 88
#5
scores.pop("Bob")
#6
for i in scores:
    print(i, ':', scores[i])
    #'Alice: 88'
    #'Charlie: 95'
    #'David: 80' 출력

#응용
students = [
    {"name" : "이대한", 'kor' : 90, 'math' : 85},
    {"name" : "박민국", 'kor' : 80, 'math' : 75},
    {"name" : "임지능", 'kor' : 95, 'math' : 90}
]
print('개인별 성적표')
print("---" * 6)
print("이름  국어  수학")
print("---" * 6)

print('개인별 평균 성적표')
print("---" * 6)
print("이름  국어  수학  평균")
print("---" * 6)

for std in students:
    sum_score = std['kor'] + std['math']
    print(sum_score)
    sum_score = std['kor'] + std['math']
    print(sum_score)
