# readlines() - 데이터를 리스트로 반환
try:
    f = open('./source/season1.txt', 'r')
    # 없는 파일을 검색
    f = open('./source/season.txt', 'r')
    # 있는 파일 검색
    seasons = f.readlines()
    # 리스트로 저장
    print(seasons) # ['봄\n', '여름\n', '가을\n', '겨울\n']

    print(seasons[0]) # 봄
    print(seasons[1]) # 여름
    print(seasons[-1]) # 가을
    print(seasons[:2]) # ['봄\n', '여름\n']

    for season in seasons:
        print(season.strip()) # 봄
    # 줄바쿰 등의 공백 제거      # 여름
                              # 가을
                              # 겨울

    for season in seasons:
        print(season)         # 봄

                              # 여름

                              # 가을

                              # 겨울
except FileNotFoundError as msg:
    # FileNotFoundError 라는 에러가 생성되면 에러 이름을 저장해
    print(msg) # [Errno 2] No such file or directory: './source/season1.txt'
    # 저장된 에러 설명을 출력
