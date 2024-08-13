# 실습 1 - 구구단 전체를 파일로 저장
f = open(r'C:\pyfile\gugudan.txt','w' )
gugudans = []

for i in range(2, 10):
    # 몇단?
    for j in range(1, 10):
        # 몇을 곱해?
        gugu = i * j
        f.write(f'{i} x {j} = {gugu} \n')
    f.write('\n')
    # 줄바꿈
f.close()

f =  open(r'C:\pyfile\gugudan.txt','r' )
print(f.read())
f.close()