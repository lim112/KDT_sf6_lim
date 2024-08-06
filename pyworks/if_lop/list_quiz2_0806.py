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
numbers.remove(min_num)
numbers.remove(max_num)
print(numbers)

print(sum(numbers) / len(numbers))

#다른버전
'''input_num = input("숫자 입력 : ").split(" ")
numbers = []
remove_numbers = []
for i in input_num:
    numbers.append(int(i))
print(input_num)

max_num = max(numbers)
print(max_num)
min_num = min(numbers)
print(sum(numbers)-max_num-min_num / (len(numbers) - 2))
'''