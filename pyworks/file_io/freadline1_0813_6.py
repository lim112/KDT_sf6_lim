# readline() : 한 줄 일기
# readlines() : 전체 줄 읽고 리스트에 반환

f = open('c:/pyfile/file.txt', 'r')
# whole = f.read()
# print(whole)

# 한 줄 읽기
line1 = f.readline()
print(line1)

# 한 줄씩 전체 읽기
while True:
    line = f.readline()
    if not line:
        break
    print(line)
    print(line.strip())
    # 공백 제거

f.close()

