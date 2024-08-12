# 실습 - 1부터 100까지 중에 4번 랜덤수를 생성,
# 생성한 수를 리스트로 출력하는
import random
i = []
for x in range(4):
    until = random.randint(1, 100)
    i.append(until)

print(i)

