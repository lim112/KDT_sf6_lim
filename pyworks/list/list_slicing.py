score = [10,20,30,40,80] #인덱싱
#print(score)

#특정한 한 개 요소에 접근
#print(score[2])

#요소 수정
print(score[2])


#슬라이싱 : 여러개 요소에 접근(콜론(:) 사용 , 최종값 -1 한 인덱스가 출력, 콜론 앞에 아무것도 안적는다면 처음부터, 0이 디폴트)
print(score[0:3]) #처음부터 3번까지
print(score[:3]) #처음부터 3번째까지
print(score[3:]) #4번째부터 마지막까지

#print(score[:])
#print(score)