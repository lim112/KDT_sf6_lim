# random 모듈
import random, math
# 랜덤 수 출력( 0.0 <= r < 1 )
print(random.random()) # 0.27840051900938

# 주사위(dice)
# 1
dice = random.randint(1,5)
print(dice) # 2

# 2 ( 다른 언어에서도 이렇게 사용 )
import math
dice2 = math.floor(random.random() * 6) + 1
print(dice2) # 6

# 주사위 10번 던지기
for i in range(5):
    dice = random.randint(1, 5)
    print(dice)

# 랜덤하게 단어 추출하기
words = [
    '나무', '책', '떡', '벌', '여룸'
]
# 방법 1
print(random.choice(words)) # 벌
# 방법 2
idx = math.floor(random.random() * len(words))
print(words[idx]) # 벌
#방법 3
idx2 = random.randint(1, len(words))
print(words[idx2]) # 벌
