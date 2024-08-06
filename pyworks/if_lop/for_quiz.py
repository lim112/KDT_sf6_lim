#실습 1
total = int(input("어디까지 더할까요?"))
for i in range(1, total):
    if i % 2 == 1:
        total += i
        print( i)

print(total)

#실습2
count = int(input("얼마나 셀까요?"))
for i in range(count, 0, -1):
    print(i, end= " ")

print("발사!")

#실습3
multiple = int(input("구구담 몇단을 할까요?"))
for i in range (1, 9):
    i += 1
    a = multiple * i
    print(f'{multiple} * {i} = {a}')

