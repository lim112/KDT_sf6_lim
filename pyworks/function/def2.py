#### 리턴(return)이 있는 함수(반환값이 있다)
#매개 변수 1개
'''def sqaure(x):
    return x * x
value = sqaure(5)
print(sqaure(3)) #9
print(value) #25

#절댓값
def my_abs(x):
    if x < 0 :
        return -x
    else:
        return x
print(my_abs(-12)) #12

print(abs(-10)) #10
print(abs(10)) #10
'''
'''def mul(x,y):
    return x * y
n = int(input("x"))
m = int(input("y"))
mul_v = mul(n,m)
print(mul(6,4)) #24
print(mul_v)'''

def my_mul(x,y):
    if x == y:
        return x * y
    else:
        return x + y
n = int(input("x"))
m = int(input("y"))
mul_v = mul(n,m)
print(mul_v)

