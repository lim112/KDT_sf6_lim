#반올림 - round(숫자 , 자리수)
# -2 : 십의 자리, -1 : 일의 자리 0 : 정수, 1 : 소수점 첫째, 2 : 소수점 둘째
round_v1 = round(2.547, 0)
print(round_v1)
print(type(round_v1))

round_v2 = round(2.547, -2)
print(round_v2)

round_v3 = round(1280, -1)
print(round_v3)

eval_v = eval('1+2')
print(eval_v)
