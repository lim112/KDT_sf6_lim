rainbow = ["red", "orange","yellow", "green","blue", "indigo","purple"]
#2번 인덱스 값 출력
print(rainbow[1])
#알바벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)
#좋아하는 개 결과 출력
rainbow.insert(-1,"gray")
print(rainbow)
"""""
rainbow.pop(3)
rainbow.pop(3)
rainbow.pop(3)
rainbow.pop(3)
rainbow.pop(3)
"""
del rainbow[3:7]

print(rainbow)

result1 = "코딩온, 저는 코딩온입니다".find("코딩온")
result2 = "코딩온, 저는 코딩온입니다".rfind("코딩온")
print(result1, result2)

sentence = 'my name is {0}. I am {1} years old'.format('hubo',6)
print(sentence)