#함수는 정의할때 동사로 정의하는 것을 추천
print('hello~~')

#인사하는 함수 - greet
def greet():
    print("안녕~~") #지역 영역
name = ['gustn','sdfk']
def greeting(name):
    print('안녕~', name)

#메인 영역(실행 영역)
greet() #안녕~~
#함수 호출

greeting(name[0]) #안녕~ gustn
#문자가 매개변수가 되어 대입

#구구단 출력하기
def is_gugu(dan):
    for i in range(1,10):
        print(f'{i} * {dan} = {dan * i}')

#구구단 호출
is_gugu(8)

def add(x,y):
    sum_v = x + y
    print(sum_v) #7
add(2,5) #매개 변수 여러개 사용하기
