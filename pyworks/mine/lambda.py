#매개 변수가 1개
#1더하기
oneup = lambda x : x + 1
print(oneup(1))
print((lambda x : x + 1 )(1))

#3배수
times = lambda x : x * 3
print(times(2))
print((lambda x : x * 3)(2))

square = lambda x : x * x
print(square(4))
print((lambda x : x * x)(4))

#매개 변수가 2개
#사칙연산
add = lambda x, y = x + y
print(add(2,3))
print((lambda x, y = x + y)(2,3)