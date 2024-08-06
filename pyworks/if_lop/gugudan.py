#구구단 3단
'''dan = int(input("몇단을 할까요? : "))
for i in range(1, 10):
    b = dan * i
    print(f'{dan} * {i} = {b}')'''

#구구단 1단부터 9단
for i in range(1, 10):
    for j in range(1, 10):
        gugudan = j * i
        print(f'{i} * {j} = {gugudan}')

    print() #줄바꿈, 엔터


#중첩 for
for i in range(1,5):
    for j in range(1,5):
        print("*", end=" ")
    print() #엔터





