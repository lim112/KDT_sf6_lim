#while true: 로 많이 씀, 무한 반복문, if ~break로 빠져나오기
'''while True:
    lunch = input("오늘 점심 메뉴?")
    print(lunch + "!!")
    if lunch == "그만":
        break
print("Done")'''

#1부터 10까지 출력
count = 0
while True:
    count += 1
    print(count, end= " ") #줄 바꿈하지않고 이어서 작성
    if count > 9:
        break # count 가 9 초과하면
print("끝")

