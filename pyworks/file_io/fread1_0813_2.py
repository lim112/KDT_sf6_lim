# 파일 읽기 - 기존의 파일 내용 일기
# 파일 열기(open()) > 쓰기(read()) > 종료(close())

f = open('C:/pyfile/file.txt', 'r')
print(f.read())
# read()안에 숫자를 적으면 해당 숫자 번째까지 반환
print(type(f.read()))