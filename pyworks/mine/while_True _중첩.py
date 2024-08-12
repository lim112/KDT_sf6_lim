exit_all = False  # 모든 루프를 빠져나가기 위한 플래그

while True:  # 바깥쪽 루프
    print("바깥쪽 루프 실행 중")

    while True:  # 안쪽 루프
        user_input = input("안쪽 루프입니다. 'exit' 입력시 전부 탈출: ")
        if user_input == "exit":
            exit_all = True  # 플래그를 설정해 모든 루프를 빠져나오게 함
            break  # 안쪽 루프 탈출

    if exit_all:
        break  # 바깥쪽 루프 탈출

    print("안쪽 루프 종료, 바깥쪽 루프 계속 실행 중")
