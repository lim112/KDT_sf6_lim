# 실습 - 1부터 100까지 중에 4번 랜덤수를 생성,
# 생성한 수를 리스트로 출력하는
import random
# i = []
# for x in range(4):
#     until = random.randint(1, 100)
#     i.append(until)
#
# print(i)

#실습 2 로또 복권 1~45, 6개 , 중복 ㄴ 0813_8
lottos = []
while True:
    lotto = random.randint(1,45)
    if lotto not in lottos:
        lottos.append(lotto)
    if len(lottos) == 6:
        break
print(sorted(lottos))

lottos2 = []
while len(lottos2) < 6  :
    a = random.randint(1,45)
    if a not in lottos2:
        lottos2.append(a)
print(sorted(lottos2))
