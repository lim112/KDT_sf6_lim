#for in 리스트
shop = ['반팔티', '바지','이어폰', '키보드']
print("바지" in shop) #'True' 출력
#바지가 리스트인 shop안에 있는지 확인하는
print('양말' in shop) #'False' 출력
print('양말' not in shop) #'True' 출력

#마우스 추가
shop.append("마우스")
print(shop) #['반팔티', '바지', '이어폰', '키보드', '마우스'] 출력

#이어폰 삭제
shop.remove("이어폰")

#여러 항목을 추가할때 
shop.extend(["커피", '비스킷'])
print(shop) #['반팔티', '바지', '키보드', '마우스', '커피', '비스킷']

#리스트에 리스트를 추가할 때
shop.append(["커피",'비스켓'])
print(shop) #['반팔티', '바지', '키보드', '마우스', '커피', '비스킷', ['커피', '비스켓']]
for i in shop: #i는 몇번째인지
    print(i)

#리스트의 연산
#개수, 합계, 평균, 최댓값, 최솟값
score = [70,60,80,80,90]
num1 = len(score)
print(f"개수 : {num1}") #'개수 : 5' 출력
print(f"합계 : {sum(score)}") #'합계 : 380' 출력
print(f'평균 : {sum(score)/len(score)}') #'평균 : 76.0' 출력
print(f'최댓값 : {max(score)}') #'최댓값 : 90' 출력
print(f'최솟값 : {min(score)}') #'최솟값 : 60' 출력

#합계
sum_v = 0
for i in score:
    sum_v += i
print(f'합계 : {sum_v}') #'합계 : 380' 출력

#최댓값
max_v = score[0] #처음으로 초기화
n = len(score)
for i in range(1, n):
    if score[i] > max_v:
        max_v = score[i]

print(max_v) #'90' 출력

n = len(score)
max_v = -99 #매우 작은 값으로 초기화
for i in score:
    if i > max_v:
        max_v = i
print(f'최댓값 : {max_v}') #'최댓값 : 90' 출력
