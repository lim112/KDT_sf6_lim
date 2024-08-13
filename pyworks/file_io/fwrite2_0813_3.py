# 입력받아서 파일 쓰기 - 추가 모드
f = open('C:/pyfile/ias.txt', 'a')
# 처음부터 추가 모드 써도 써지기는 함
text = input('글자 입력 : ')
f.write( text + '\n' )

f.close()

#
