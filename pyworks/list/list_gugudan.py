#구구단 프로그램 구현 - 리스트
dan = 2
mul = []
gugu = []
for i in range(1,10):
    gugu.append(dan * i)
    mul.append(i)
#print(gugu)
for j in range(1,9):
    print(f'{dan} * {mul[j]} = {gugu[j]}')

#간결 버전 리스트에 추가하면서
for i in range(1, 10):
    gugu.append(dan * i)
    print(f'{dan} * {i} = {gugu[i-1]}')
    #i-1을 하는 이유 범위가 달라지기 때문

#리스트에 추가하지 않는 구구단
gu = 0
for i in range(1, 10):
    print(f'{dan} * {i} = {dan * i}')

#구구단 전체 출력
gugudan = []
row = [] #해당 구문을 i for구문 안에 넣는다면 한단씩만 저장하여 출력할 수 있다
for i in range(2,10):
    row = []
    for j in range(1,10):
        row.append((i * j))
        print(f'{i} * {j} = {row[j - 1]}')
    print()
#    print(row)
#print(j)
#print(i)
