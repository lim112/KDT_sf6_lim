#자리배치도
#고객수 - customer, 좌석열 - column, 행 - row
#나눠떨어지면 행 추가 ㄴㄴ 나눠떨어지지 않으면 행 추가
#나머지가 0일때 행의수 0이 아닐때 행의 수 분기
customer = int(input("고객 수 입력 : "))
column = int(input("고객 열 수 입력 : "))
if customer% column == 0:
    row = customer// column #몫
else:
    row = customer// column + 1

for i in range(0, row):
    for j in range(1, column + 1):
        num = i *column + j
        if num > customer:
            break
        print(num, end=" ")
    print()

