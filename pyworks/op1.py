#연산자(operator)
#산술 연산 - +, -, *, / ,//(몫) , %(나머지)
n1 = 10
n2 = 20

#산술 연산

#출력
print( n1 , n2)
print( n1 + n2)
print( n1 - n2)
print( n1 * n2)
print( n1 / n2)
print( n1 // n2)
print( n1 % n2)

print( n1 ** n2)
print( 2**3)

sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2

print(sum)
print(sub)
print(mul)
print(div)

#실습 30개 빵을 4명이서 나눠먹을때 인당 빵 개수와 나머지
bread = 30
human = 4
share = int(bread / human)
rest = bread % human
print( '빵의 개수 : ' , share)
print( '남는 빵의 개수 : ' ,rest)
나머지 = ( '남는 빵의 개수 : ' + str(rest))
print(나머지)
