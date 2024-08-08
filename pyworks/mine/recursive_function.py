#재귀함수 - recursive function

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

sos(5)
