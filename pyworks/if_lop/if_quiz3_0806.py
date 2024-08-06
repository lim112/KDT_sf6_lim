'''age = int(input("나이를 숫자로 입력해주세요 : "))
pay = input("결재 방법을 입력해주세요(카드 또는 현금만 입력) : ")
money
if age < 8 :
    money = '무료'
elif age < 14 and age >= 8 :
    money = 450
elif age >= 14 and age < 20 :
    if pay == "카드":
        money = 720
    else :
        money = 1000
elif age >= 20 and  age < 75:
    if pay == "카드":
        money = 1200
    else:
        money = 1300

else :
    money = "무료"

print(f'{age}의 {pay} 요금은 {money}원 입니다')
'''

#실습 5
#sum()
print(sum([1 , 2, 3]))
print(max([1,2,3]))
input_num = input("숫자 입력 : ").split(" ")
numbers = []
remove_numbers = []
for i in input_num:
    numbers.append(int(i))
print(input_num)

max_num = max(numbers)
min_num = min(numbers)
numbers= numbers.remove(max_num)
remove_numbers = numbers.remove(min_num)
print(sum(remove_numbers) / len(remove_numbers))