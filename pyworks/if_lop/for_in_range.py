#for 반복문
'''
for i range(시작값, 종료값+1, 종료값)
    실행문
'''

a = range(10)
print(list(a))

b = range(1,11)
print(list(b))

c = range(1,11,2)
print(list(c))

#for문 1부터 10까지 출력
for i in range(1, 11):
    print(i, end = " ")

#for문 1부터 10까지 더하기
total = 0
for i in range(1, 11):
    print("i = ", i, "total = ", total)
    total += i

print(total)


