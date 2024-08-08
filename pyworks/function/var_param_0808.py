#기본 매개 변수
#매개 변수의 입력 없이 정해지지 않으면 변수 이름 앞에 *를 붙힌다
def calc_avg(numbers):
    sum_v = 0
    for i in numbers:
        sum_v += i
    return sum_v / len(numbers)

avg1 = calc_avg(1,2)
print(avg1)

avg2 = calc_avg(1,2,3,4)
#numebrs 의 리스트 안에 숫자들이 있다고 생각하면 될 듯, 다만 numbers를 프린트하면 안나타남
print(avg2)
