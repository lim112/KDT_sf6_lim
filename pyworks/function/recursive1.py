#재귀함수 - recursive function
'''
def sos1(n1):
    for i in range(n1):
        print('hello')
sos1(5)

#위의 함수를 재귀함수 형태로 쓰면 아래 형태가 된다
def sos(n):
    print('help me!!')
    if n == 1:
        return ''
    else:
        return sos(n-1)

sos(5)'''

#팩토리얼 계산
def facto1(n):
#재귀함수를 사용하지 않는 방식
    f = 1
    for i in range(1, n):
        f *= i
    print(f)
facto1(5)

def facto(n):
    if n == 1:
        return 1 #종료조건, 종료조건은 충분히 작을것
    else:
        return n * facto(n-1)

print(facto(5))
