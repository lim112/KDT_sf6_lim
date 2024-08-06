'''exam = int(input("점수 입력 : "))
grade = ""
if exam >= 90 :
    print("A등급입니다")
elif exam >= 80 and exam < 90 :
    print("B등급입니다")
elif exam >= 70 and exam < 80 :
    print("C등급입니다")
elif exam >= 60 and exam < 70 :
    print("D등급입니다")
else:
    print("E등급입니다")

#elif exam < 60 :
#   print("E급 입니다")'''

#8월 6일
#점수가 마이너스가 입력될 경우
'''while True :
    exam = int(input("점수 입력 : "))
    if exam >= 0 :
        break
grade = ""
if exam >= 90 :
    print("A등급입니다")
elif exam >= 80 and exam < 90 :
    print("B등급입니다")
elif exam >= 70 and exam < 80 :
    print("C등급입니다")
elif exam >= 60 and exam < 70 :
    print("D등급입니다")
else:
    print("E등급입니다")'''

#다른 버전
while True:
    exam = int(input("점수 입력 : "))
    if exam >= 0:
        if exam >= 90:
            print("A등급입니다")
        elif exam >= 80 and exam < 90:
            print("B등급입니다")
        elif exam >= 70 and exam < 80:
            print("C등급입니다")
        elif exam >= 60 and exam < 70:
            print("D등급입니다")
        else:
            print("E등급입니다")
    else:
        print("올바른 점수를 입력해주세요")