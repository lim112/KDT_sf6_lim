'''
#다중조건문 - if,elif, else
age = 29
if age >= 0 and age < 20:
    print("미성년자 입니다")
elif age >= 20 and age < 30:
    print("20대 입니다")
elif age >= 30 and age < 40:
    print("30대 입니다")
else:
    print("이제는 중년....")

print( f"나이는 {age}세 입니다")"

'''

age = int(input("나이를 입력하세요 "))
gender = input("여 or 남으로 입력해주세요 : ") #남/여
if age >= 0 and age < 20:
    print("미성년자 입니다")
elif age >= 20 and age < 30:
    if gender == "여":
        print('20대 여성입니다')
    else:
        print("20대 남성입니다")
elif age >= 30 and age < 40:
    if gender == "여":
        print('30대 여성입니다')
    else:
        print("30대 남성입니다")
else:
    if gender == "여":
        print('40대 여성입니다')
    else:
        print("40대 남성입니다")

print( f"나이는 {age}세 입니다")
