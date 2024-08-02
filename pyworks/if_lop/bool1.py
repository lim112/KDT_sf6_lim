#비교 연산 - >, <=, < >=, ==, !=
#비교 연산의 결과는 -bool자료(true/false)
b1 = 2 >1
print(b1) #true
print(type(b1))
b2 = (2 == 1)
print(b2)
b3 = not(2 == 1)
print(b3)

#논리 연산 - and, or, not
logig1 = (2 > 1) and (2 == 1)
#and연산 - and양쪽에 있는 조건이 둘 다 true일때 결과 true
print(logig1)

logig2 =  (2 > 1) or (2 == 1)
#or연산 - or양쪽에 있는 조건이 하나만 true여도 참 결과 true
print(logig2)

logig3 = not(2 != 1)
print(logig3)

#논리연산예제
age = 17
under_20 = age < 20
print(under_20)
