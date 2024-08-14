try:
    with open('./output/input.txt', 'a') as f:
        # 만약 파일이 없다면 생성된다 ( 'a', 'w' 둘 다 )
        while True:
            text = input('저장할 내용을 입력하세요(종료 ~ z) : ')
            if text == 'z' or text == 'Z':
                break
            f.write(text)
            f.write('\n')
except:
    print('파일을 찾을 수 없습니다')