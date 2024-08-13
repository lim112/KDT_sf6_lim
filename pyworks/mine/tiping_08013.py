import random, time
words = [
    'sky', 'shirt','moon','earth', 'tree', 'apple','grape', 'garlic', 'onion', 'potato'
]

count = 1 # 문제 번호
start_t = time.time()
# while count < 11:
#     # 문제 번호
#     print(f'문제 {count}')
#     count += 1
#     while True:
#         # rand_n = random.randint(1, len(words) - 1)
#         #choice_word = words[rand_n]
#         choice_word = random.choice(words)
#         print(choice_word)
#         typing = input('')
#         if typing == choice_word:
#             print('정답')
#             break
#         # elif typing != choice_word:

n = 1
collects = []
while count < 11:
    print(f'문제 {count}')
    question = random.choice(words)
    # if question in collects:
    #     break
    while count < 11:
        if question in collects:
            # 안나왔던 단어만 출력
            break
        user = input()
        # 유저가 단어 입력
        if user == question:
            print('통과!!')
            count += 1
            collects.append(question)
            break
        else:
            print('오타! 다시 도전')
            print(question)
            # 랜덤으로 문제 출력

end_t = time.time()
et = end_t -  start_t
print('프로그램 종료')
print(f'타자 게임 : {et}초') # 시작 시간과 끝난 시간의 시간 간격을 출력
