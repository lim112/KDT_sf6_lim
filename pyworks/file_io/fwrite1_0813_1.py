# 파일 쓰기 - 파일 생성
# 파일 열기 (open()) > 파일 쓰기(write()) > 종료(close())
# 절대 경로(C:\디렉토리/파일) : ex) C:\pyfile
# 상대 경로
# 모드(mode) - 쓰기('w') 모드, 읽기('r') 모드, 추가 모드('a')
# ex) f = open('경로', '모드')

# 문자(글자)를 쓰기 (저장)
f = open('C:/pyfile/file.txt', 'w')
# C:/pyfile에 file.txt 파일을 생성

f.write('hello python!!\n')
# 위 파일에 'hello python!!\n' 쓴 뒤 줄바꿈
f.write('너무 더워!!\n')
# 위 파일에 '너무 더워!!\n' 쓴 뒤 줄바꿈

#숫자 저장
f.write('1\n') # 파일에 '1' 입력
# f.write(1) # TypeError: write() argument must be str, not int
# 숫자는 입력 불가, 문자로 바꿔 입력
num = 4 + 5
# 계산해야한다면 저장전에 계산
f.write(f'{num}\n')


# 한자도 입력 가능
# f.write('賢') # 파일에 '賢' 입력
# 만약 쓰기에서 어떤 과정을 삭제한다면 수정되어 저장됨 > 새로 저장
f.close()