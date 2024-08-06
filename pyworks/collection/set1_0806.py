#set - 인덱싱 불가(순서가 없다), 중복된 항목 추가 불가 {}
cart = ["양파" ,"쌀", "콩나물", "쌀"]
print(cart) #['양파', '쌀', '콩나물', '쌀'] 출력

cart = {"양파" ,"쌀", "콩나물", "쌀"}
print(cart) #{'쌀', '양파', '콩나물'} 출력

#print(cart[0])

#빈 집합(set)생성
s1 = set() #set() 함수 생성
print(s1) #set() 출력
s1.add("a")
s1.add("b")
s1.add("c")
print(s1) #{'b', 'a' 'c'} 출력
s1.remove("b")
print(s1) #{'c', 'a'} 출력

"""
s1.clear()
print(s1) #set()
"""

print("a" in s1) #True 출력
print("d" in s1) #False 출력
