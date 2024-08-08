#실습3 자판기 프로그램 함수화
vending_machine = ['게토레이', '레쓰비', '생수', '이프로', '생수', '게토레이']
'''def is_vending_machine(x):
    while True:
        print(vending_machine)
        print("사용자의 종류를 입력하세요 \n1.소비자 \n2.주인")
        person = int(input())
        if person == 2:
            print("할 일 선택 : \n1.추가 \n2.삭제")
            master = int(input())
            if master == 1:
                print(f"추가 \n남은 음료수 : {vending_machine} \n")
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
                        print("음료수를 확인해주세요 \n", vending_machine)
        elif person == 1:
            drink = input("마시고 싶은 음료수 : ")
            if drink in vending_machine:
                print(f'{drink} 드릴께요')
                vending_machine.remove(drink)
            else:
                print(f'{drink}는 지금 없네요')

#is_vending_machine()
#commands =[    'check' : '남은 음료수를 확인할 수 있는 함수']

#command = input()
def check_machin(x):
    if x in vending_machine:
        return '남아있습니다'
    else:
        return '없습니다'
check_m = check_machin(input('어떤 음료수를 찾으세요?'))
#이렇게만 쓰면 리턴값이 어떤지 확인할 수 없기 때문에 아래 코드를 추가한다
print(f'해당 음료수는 {check_m}')'''


while True:
    count = 0
    print(1)
    print(count)
    count += 1
    if count > 10:
        while True:
            count += 2
            print(2)
            print(count)
            if count > 20:
                while True:
                    count += 3
                    print(3)
                    print(count)
                    if count > 30:
                        while True:
                            count += 3
                            print(4)
                            print(count)
                            if count < 40:
                                break
                            print(5)
                            break
                    print(6)
                    break
            print(7)
            break
    print(8)
    break
#while True 에서 break를 쓸때 한겹만 벗겨질까?

#각각을 함수를 자유롭게 옮겨다니려면 함수안에 함수를 만들던가 매개변수를 만드는게 나을듯

