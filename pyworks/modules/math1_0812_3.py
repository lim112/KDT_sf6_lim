import math, datetime
# 수학 관련 내장 모듈 - math 사용

print(math.pi) #3.141592653589793

#원의 넓이(area)
redius = 6
area = redius * redius * 3.14
print(area) #113.04
area2 = redius * redius * math.pi
print(area2) #113.09733552923255
# 완전히는 아니지만 상대적으로 정확

# 올림 - 1을 더해서 정수로 변환
print(math.ceil(2.45)) # 3

# 버림(내림) - 소수점 이하를 버리고 정수로 변환
print(math.floor(2.45)) # 2

# 제곱근(루트) - 제곱근을 실수로 변환
print(math.sqrt(25)) # 4.898979485566356

# 반올림(내장함수) - round(x, y) y : 1 소수 첫째 자리까지, 0 : 소수 버림, -1 : 1의 자리 버림
print(round(2.57, -1))

