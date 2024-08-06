#유용한 문자열 함수
#문자의 개수, 항목의 개수 - len(), 중복된 문자 개수 - count()
#대문자 변환 - 문자열.upper(), 소문자 - 문자열.lower()
#문자열을 잘라서 리스트로 변환 - 문자열.split(구문자)
#특정한 문자를 변경 - replace(old, new)
'''
f = ["바나나", "banana"] #항목의 개수 세기
print(len(f))

l = "바나나"
print(len(l))

dupl_count = "banana"
print(dupl_count.count("a"))
print("banana".count("a"))
'''
'''
#대소문자 만들기
upper_case = "Hello".upper()
print(upper_case)
lower_case = "HELLo".lower()
print(lower_case)

#문자열을 잘라서 리스트로 변환 - 문자열.split(구문자)
friends = "존 루나 제리"
print(friends.split(" "))

alpha = "a:b:c:d"
print(alpha.split(":"))

email = "coding0n@spreatics.com"
print(email.split("@"))

#리스트에서 특정 번째를 여러개 변경
q = [1,2,3,4,5,6,7,8,9,10,11,12,13]
q[2:5] = [12,13,14,15]
print(q)

#특정한 문자를 변경 - replace(old, new)
msg = "hello python"
print(msg.replace("python", "c++"))
'''
#0806
input_num = input("숫자 입력 : ").split(" ")
numbers = []
for i in input_num:
    numbers.append(int(i))
print(input_num)
print(numbers)