#리스트 함수
#추가 - 리스트.append() 마지막에 추가, 리스트.insert() 특정한 번째에 추가
#삭제 - 리스트.pop() 마지막 인덱스 삭제, 리스트.remove() 특정 항목 삭제
#정렬 - 리스트.sort(), 뒤집기 - reverse()
lower = ["a", "b", "c","d"]

#e추가
lower.append("e") #맨 뒤 인텍스에 추가
print(lower)

#e삭제
lower.pop() #맨 뒤 삭제
print(lower)

#특정 번째 추가
lower.insert(2, "e")
print(lower)

#특정 항목 삭제
lower.remove("c")
print(lower)

#내림차순 아스키 코드 순서대로
lower.sort()
print(lower)

#거꾸로
lower.reverse()
print(lower)