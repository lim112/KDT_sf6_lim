#자판기
vending_machine = ['케토레이', '레쓰비', '생수', '이프로']

while True:
    print(vending_machine)
    print("사용자의 종류를 입력하세요")
    print("1.소비자")
    print('2.주인')
    person = int(input())
    if person == 1 :
        print("할 일 선택 : ")
        print("1.추가")
        print("2.삭제")
        master = int(input())
        if master == 1:
            print("추가")
            print(f"남은 음료수 : {vending_machine}")
            print()
            add_drink = input("추가할 음료수? ")
            vending_machine.append(add_drink)
        elif master == 2:
            remove_drink = input("삭제할 음료수? ")
            while True:
                if remove_drink in vending_machine:
                    vending_machine.remove(remove_drink)
                    print("삭제완료")
                    break
                else:
                    print("음료수를 확인해주세요")
                    print(vending_machine)
    elif person == 2 :
        drink = input("마시고 싶은 음료수 : ")
        if drink in vending_machine:
            print(f'{drink} 드릴께요')
            vending_machine.remove(drink)
        else:
            print(f'{drink}는 지금 없네요')


