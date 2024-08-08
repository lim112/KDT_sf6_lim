#리스트를 매개 변수로 사용 함수

v = [1,2,3,4]
def times(a):
    a2 = []
    for i in a:
        a2.append( i * 3)
    return a2
v2 = times(v)
#a와 v, 매개변수의 단어는 달라도 대입된다 호출 안에 들어가는게 중요
print(v2)

#다른 방식
def times2(a):
    a2 = [i * 3 for i in a] #리스트의 생성과 관리를 동시에
    return a2

v3 = times2(v)
print(v2)

