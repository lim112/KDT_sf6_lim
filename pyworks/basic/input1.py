#입력 함수 - input(문자)
##name = input("이름 입력 : ")
##print("당신의 이름은 " + name + "이군요")

number = input("숫자 입력 : ")
print( int(number) + 1)

num1 = input("첫번째 수 입력 : ")
num2 = input("두번째 수 입력 : ")
print( num1 + num2 )
print(type(num1))
print(float(num1) + float(num2))

num3 = int(4.5)
print(num3)

#오류처리(try ~except 구문)
#try :
#    실행문(오류 가능성이 있는 구문
#except:
#    오류 처리구문


'''
def test():
    try:
        num1 = input("첫번째 수 입력 : ")
        if type(num1) == str:
            print('정수를 입력해주세요')
            test()
        num2 = int(input("두번째 수 입력 : "))
        if type(num2) == str:
            print('정수를 입력해주세요')
            #test()
        print( int(num1) + int(num2))
    except ValueError:
        print(float(num1) + float(num2))
    except UnboundLocalError:
        print('정수를 입력해주세요')
        
        print("숫자를 입력해주세요")

test()

'''
