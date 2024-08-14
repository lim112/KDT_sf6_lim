# 숫자 추측 게임 (범위 : 1 ~ 100 )
import random
count = 0
#컴의 랜덤값
num_rand = random.randint(1,100)
while True:
    count += 1
    try:
        if count == 1:
            choice_num = int(input(f'숫자 입력([{count}]회 1 ~100 : '))
            if choice_num == num_rand:
                break
        else:
            if choice_num > num_rand:
                print('랜덤수보다 커요')
                choice_num = int(input(f'숫자 입력([{count}]회 {choice_num} ~100 : '))
            elif choice_num < num_rand:
                print('랜덤수보다 작아요')
                choice_num = int(input(f'숫자 입력([{count}]회 {choice_num} ~100 : '))
            if choice_num == num_rand:
                break
        if choice_num > 100 or choice_num < 0 :
            print('입력 범위를 초과 했어요')
            if choice_num > 100 :
                choice_num == 100
            elif choice_num < 0:
                choice_num == 0
    except:
       print('숫자만 입력해주세요')


# 리더님 버전
com = random.randint(1,100)
min_v =1
max_v = 100
count = 0
while True:
    count = count + 1
    try:
        #서식 대응 문자 - %d, %f, %s
        guess = int(input('숫자 입력 (%d ~ %d ) : ' % (min_v, max_v)))
        if com == guess:
            print('정답입니다')
            break
        elif com > guess:
            print('랜덤수보다 작아요')
            min_v = guess
        elif com < guess:
            print('핸덤수보다 커요')
            max_v = guess
    except ValueError:
        print('숫자만 입력해주세요')

# 전 아직 갈길이 멉니다


