# 명령행(command line)에서 인수 전달
import sys
print(sys.argv)
# argv 속성은 입력된 자료를 리스트로 반환
args = sys.argv[1:] # 0번 제외 - 파일 이름

# 터미널에서 python sys1_0812_8.py dog을 입력하면 [sys1_0812_8.py, dog]으로 리스트에 담김
# python 뒤 처음은 파일 이름이 올 것
print(args)

# 입력값의 합계와 평균 계산
total = 0
for i in args:
    total += int(i)
    # 터미널에서 입력되는건 문자로 입력됨

print(f'합계 : {total}')
print(f' 평균 : {total/ len(args)}')