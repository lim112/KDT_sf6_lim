# #실습1 주어진 수(2,2)가 같다면 곱, 수(2,3)가 다르다면 합
# def my_mul(x,y):
#     if x == y:
#         return x * y
#     else:
#         return x + y
#
# mine = my_mul(2,2)
# print('두수의 곲 :' ,mine) #두수의 곲 : 4
# mine = my_mul(2,3)
# print('두수의 합 :', mine) #두수의 합 : 5
#
# def my_mul(x,y):
#     if x == y:
#         return x * y
#     else:
#         return x + y
# for i in range(2):
#     n = int(input("x"))
#     m = int(input("y"))
#     mul_v = my_mul(n,m)
#     print(mul_v)

gob_v = 1
def gob_n(n):
    global gob_v #함수안에서 쓸거라고 선언
    for i in range(1, n + 1):
        gob_v *= i
    return gob_v
print(gob_n(3)) # 6

#print('결과값 :', gob_n(6))
#4! = 4*3*2*1(팩토리얼)


def multiple(divide):
    count = 0
    print()
    for j in range(30):
        if j % divide == 0:
            print(j ,  end= " ")
            count+= 1
    print()
    #쓰지말고 \n을 f포맷 안에 사용하면 줄이 바꿔지낟
    #\n 줄바꿈, \t 탭
    return count

d = int(input("어떤 수의 배수의 수를 구할까요? "))

print(f'{d} 의 배수 : {multiple(d)}')