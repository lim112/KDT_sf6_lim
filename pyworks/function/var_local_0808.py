#지역 변수, 매개 변수

num1 = 10
num2 = 20
total = num1 + num2
#스택 구조 : 먼저 들어간게 나중에 빠지는 구조
'''
메모리에서 생성 순서
1.num1
2.num2
3.total

메모리에서 소멸 순서
1.total
2.num2
3.num1
'''

def calc():
    x = 2 * num1
    print('x =', x)

calc()
