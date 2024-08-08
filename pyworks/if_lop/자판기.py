#자판기
'''#자판기 과제 1
vending_machine = ['케토레이', '레쓰비', '생수', '이프로']
while True:
    print('=====================RESTART')
    drink = input("마시고 싶은 음료? ")
    if drink in vending_machine:
        print(f'{drink} 드릴께요')
        vending_machine.remove(drink)
    else:
        print(f'{drink}는 지금 없네요')
vending_machine = ['케토레이', '레쓰비', '생수', '이프로']'''

#자판기 과제 2
vending_machine = ['게토레이', '레쓰비', '생수', '이프로', '생수' , '게토레이']
def is_vending_machine():
    while True:
        print(vending_machine, '\n사용자의 종류를 입력하세요 \n1.소비자 \n2.주인')
        person = input()
        if person == "2" :
            print("할 일 선택 : \n1.추가 \n2.삭제")
            master = input()
            if master == '1':
                print(f"추가 \n남은 음료수 : {vending_machine} \n")
                add_drink = input("추가할 음료수? ")
                vending_machine.append(add_drink)
            elif master == '2':
                remove_drink = input("삭제할 음료수? ")
                if remove_drink in vending_machine:
                    vending_machine.remove(remove_drink)
                    print("삭제완료")
                else:
                    print("해당 음료수는 없습니다 확인해주세요 \n")
        elif person == '1' :
            drink = input("마시고 싶은 음료수 : ")
            if drink in vending_machine:
                print(f'{drink} 드릴께요')
                vending_machine.remove(drink)
            else:
                print(f'{drink}는 지금 없네요')

is_vending_machine()

def check_machin(what):
    if what in vending_machine:
        return '남아있습니다'
    else:
        return '없습니다'
check_m = check_machin(input('어떤 음료수를 찾으세요? '))
#이렇게만 쓰면 리턴값이 어떤지 확인할 수 없기 때문에 아래 코드를 추가한다
print(f'해당 음료수는 {check_m}')
def is_drink():
    what = input('어떤 음료수를 확인하시겠어요? ')
    if what in vending_machine:
        return '해당 음료수은 있습니다'
    else:
        return '해당 음료수는 없습니다'
is_drink()
def add_drink():
    what = input('어떤 음료수를 추가하시겠어요? ')
    vending_machine.append(what)
add_drink()
def remove_drink():
    what = input("어떤 음료수를 제거하시겠어요? ")
    if what in vending_machine:
        vending_machine.remove(what)
        print('해당 음료수를 제거하였습니다')
    else:
        print('해당 음료수는 없습니다 확인하여 주세요')
remove_drink()


