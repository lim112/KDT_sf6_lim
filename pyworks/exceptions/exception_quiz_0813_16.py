# 실습 1 정수 입력 받기 - 예외 처리
#1
while True:
    try:
        i = int(input('숫자 입력'))
    except ValueError:
        print('정수가 아닙! 정수를 입력해주세요')
    else:
        print(f'정수 입력 성공 : {i}')
        break
#2
while True:
    try:
        i = int(input('숫자 입력'))
        # 정수라면 try 안에서 계속 진행된다
        # 정수가 아니라면 바로 벗어나 except로 넘어감(i에 저장되지 않는다)
        print(f'정수 입력 성공 : {i}')
        break
    except ValueError:
        print('정수가 아닙! 정수를 입력해주세요')


