#리스트의 복사 (새로운 리스트 생성)
a = [1,2,3,4]
a2 = []
a3 = []

#a 복사하기
for i in a:
    a2.append(i)

print(a2)
#list 내 for, append
a6 = [i for i in a2]
print(a6) #[1, 2, 3, 4] 출력

#a복사해서 3곱하여 저장하기
for i in a2:
    a3.append(i*3)
print(a3) #[1, 2, 3, 4], [3, 6, 9, 12] 출력

#list 내 for
#[표현식 for 요소 in 리스트]
a4 = []
a4 = [i*3 for i in a2]
print(a4) #[3, 6, 9, 12] 출력

#3의 배수이면서 짝수인 수 저장
a5 =[] #표현식 반복문 조건
a5 = [i*3 for i in a2 if i % 2 == 0]
print("a5 = ", a5) #a5 =  [6, 12] 출력

