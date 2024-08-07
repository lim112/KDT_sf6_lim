'''a= [1,2,3,4]
total = 0
for i in a:
    total += i

print(total) #10
print("합계 :" ,total) #합계 :  10
print("평균 :", total / len(a))  #평균 :  2.5
'''
#이차원 리스트의 평균과 합계
d = [
    [1],
    [2,3],
    [4,5,6]
]
sum_v = 0
count = 0
for i in range(len(d)):
    for j in range(len(d[i])):
        sum_v = sum_v + d[i][j]
        count += 1
print(sum_v) #21
print("합계 :", sum_v) #합계 : 21
print('평균 :', sum_v / count) #평균 : 3.5

'''sum_v = 0
for i in d:
    #for j in d[i]:
    sum_v += i

print(sum_v)'''