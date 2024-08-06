''''#중첩 for
for i in range(1,5):
    for j in range(1,5):
        print("*", end=" ")
    print() #엔터
'''
#별하나씩 더해 가기
#중첩 for
'''
for i in range(6, 1, -1):
    for j in range(5, 6 - i, -1):
        print("*", end= "")
    print()
'''

#단일 for
for i in range(6, 0, -1):
    print("*" * i) #문자도 곱하기가 됨 > i 번 작성
    #pass #나중에 쓸텐데 지금 실행하면 오류나기 때문에
print()

#우측에 붙은 *
for i in range(1, 5):
    print(" " * (4-i), "*" * i )

#좌석수
#숫자가 연속으로 증가하는 알고리즘
for i in range(0, 4):
    for j in range(1,5):
        num = i * 4 + j
        if num > 15:
            break
        print(num," ", end = "")
    print()

