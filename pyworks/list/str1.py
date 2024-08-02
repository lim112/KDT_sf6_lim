'''#문자열은 특별한 1차원의 리스트이다
msg = "Have a nice day"
print( msg[0])
print(msg[-1])
print(msg[:4])
print(msg[7:])
'''
#문자열 포맷 서식
# %d - 정수 ,%s - 문자열, %f - 실수
print("나는 이번 달에 책을 %d 샀어요" % 2) #%를 기준으로 우측의 항목이 대입된다
print("나는 이번 달에 책을 %s 샀어요" % "두")

count = 2
print("나는 이번 달에 책을 %r권 샀어요" % count)
cost = 50000
print("나는 이번 달에 책을 %d권 샀어요, 비용은 %d원 들었어요" % (count,cost)) #항목 여러개가 대입될때는 괄호처리

#1인치 - 2.54cm
print("1인치는 %.2fcm입니다" % 2.54)
ch = 2.540000
print(f"1인치는 {ch:.2f}cm입니다")