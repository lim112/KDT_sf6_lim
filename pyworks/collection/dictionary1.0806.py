# 자료구조 - 딕셔너리(dictionary) c 생성,r 조회,u 수정,d 삭제
# '치킨' : '닭을 튀긴 요리' 이렇게 매칭 시키는 것, key:value
# {} 중괄호 사용
#fruits = ['apple', 'banana', 'cherry']
fruits = {
    'apple' : '사과', 'banana' : '바나나', 'peach' : '복숭아'
}

#접근
print(fruits["apple"]) #'사과' 출력
#print(fruits["tomato"]) #없는거 검색하면 오류

#get()을 이용한 검색
print(fruits.get("banana")) #'바나나' 출력
print(fruits.get("tomato")) #'None' 출력

#요소 추가
fruits["strawberry"] = "딸기"
print(fruits) #{'apple': '사과', 'banana': '바나나', 'peach': '복숭아', 'strawberry': '딸기'}
print(type(fruits)) #<class 'dict'> 출력

#요소 변경
fruits["peach"] = ["천도복숭아", "복숭아"]
print(fruits) #{'apple': '사과', 'banana': '바나나', 'peach': ['천도복숭아', '복숭아'], 'strawberry': '딸기'}
print(fruits["peach"][1]) #'복숭아' 출력

#요소 삭제
fruits.pop("banana")
print(fruits) #{'apple': '사과', 'peach': ['천도복숭아', '복숭아'], 'strawberry': '딸기'} 출력

#키만 반환
print(fruits.keys()) #{'apple': '사과', 'peach': ['천도복숭아', '복숭아'], 'strawberry': '딸기'} 출력

#키와 값 반환
print(fruits.items()) #전체는 리스트로 구정 그안에 키와 값이 튜플로 구성 |
# dict_items([('apple', '사과'), ('peach', ['천도복숭아', '복숭아']), ('strawberry', '딸기')]) 출력

for key in fruits:
    print(key + ":" ,fruits[key])
        #apple: 사과
        #peach: ['천도복숭아', '복숭아']
        #strawberry: 딸기 출력

#다른 버전
for key in fruits.keys(): #어차피 key를 찾아서 매칭되는 것을 찾는것이기에
                            #빼도 상관 없음
    print(key + ":" ,fruits[key])

#딕셔너리 생성
dict1 = {1: 'a', 2 : 'b', 3 : 'c'}
print(dict1) # {1: 'a', 2: 'b', 3: 'c'} 출력

# key = 4, value = "d" 추가
dict1["4"] = "d"
print(dict1) #{1: 'a', 2: 'b', 3: 'c', '4': 'd'} 출력

#for 문을 이용한 전체 조회
for key in dict1.keys(): #dict1(): 사용 가능
    print(key, ':', dict1[key])
    #1 : a
    #2 : b
    #3 : c
    #4 : d 출력

#문제
#요소 수정 - key 3을 k로 변경
dict1[3] = "k"
print(dict1) #{1: 'a', 2: 'b', 3: 'k', '4': 'd'} 출력

#요소 삭제 - key 2 삭제
dict1.pop(2)
print(dict1) #{1: 'a', 3: 'k', '4': 'd'}출력

#빈 딕셔너리 생성
dict2 = {}
print(type(dict2)) #<class 'dict'> 출력



