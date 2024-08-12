# time 모듈
# time.time() - 1970년 자정이후부터 시간을 초로 반환
import math
import time

print(time.time()) #1723462560.789995
day = time.time() / (60 * 24 * 60)
print(math.floor(day)) # 19947
year = time.time() / (365 * 24 *60 * 60)
print(math.floor(year)) # 54

# for i in range(11):
#     print(i)
#     time.sleep(1)
#     #1초 간격으로 숫자 출력

#수행(실행) 시간 측정
# start = time.time() #시작 시간
# for i in range(11):
#     print(i)
#     time.sleep(1)
# end = time.time() #시작 시간
# among = end - start

start = time.time() #시작 시간
for i in range(1000000):
    print(i)
end = time.time() #시작 시간
print(end-start)


