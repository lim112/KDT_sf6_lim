#튜플 - 소괄호 읽기 전용 수정 삭제 안됨, 단 요소가 한개라면 적용되지 않는다
t1 = (10,20,30, 10)
print(t1) #'(10, 20, 30)' 출력
print(type(t1)) #<class 'tuple'> 출력
print(t1[0]) #대괄호는 인덱싱한다는 뜻 '10' 출력
print(t1[1:3]) #'(20, 30)'출력

#수정안됨
#t1[1] = 50

t3 = (7,) #소괄호 안에 쉼표가 들어가면 튜플로 적용
print(t3) #(7,)
print(type(t3)) #<class 'tuple'>

#튜플 합계
#print(sum(10,20,30))

#튜플 최솟값
print(min(10,20,30)) #10

#튜플 항목 더하기
tu1 = (1,2,[4,5,6])
tu2 = (4, )
tu3 = tu1 + tu2
print(tu3) #(1, 2, [4, 5, 6], 4)
print(tu3[1:]) #(2, [4, 5, 6], 4)