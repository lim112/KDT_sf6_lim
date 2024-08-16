# 영어 단어장 만들기
# 경로 - game 폴더에 위치함, 단어장 파일 - words.txt
import random
import time

with open('words.txt', 'w') as f:
    words = ['sky', 'shirt', 'moon', 'earth', 'tree',
             'apple', 'grape', 'garlic', 'onion', 'potato']
    for i in words:
        f.write(i + ' ')

count = 1  # 문제 번호
with open('words.txt', 'r') as f:
    data = f.read().split()
    # f.read()는 각 변수로 적용 두번 쓰면 안됨
    #공백제거, 리스트로 저장
    #print(data)
    word = random.choice(data)
    start_t = time.time()
    count = 1
    while count < 11:
        print(f'문제 {count}')
        question = random.choice(words)
        print(question)
        # if question in collects:
        #     break
        while count < 11:
            user = input()
            # 유저가 단어 입력
            if user == question:
                print('통과!!')
                count += 1
                break
            else:
                print('오타! 다시 도전')
                print(question)
                # 랜덤으로 문제 출력

    end_t = time.time()
    et = end_t - start_t
    print('프로그램 종료')
    print(f'타자 게임 : {et}초')  # 시작 시간과 끝난 시간의 시간 간격을 출