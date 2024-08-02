# 변수
floor = 6541688614632132138897 #정수를 저장하는 floor라는 변수 '=' 하나는 대입연산자
name =  '임현수'
weight =6.7

#print("나는", floor,"층에 살아요", sep=' ' )
#f 포멧 방식 출력 - 변수는 {}중괄호 안에 넣는다
print( f'나는 {name}충에 살아요')
print(name)
print("내 이름은 " + name + "입니다")

#를 넣을때는 중간에 다른 유형의 변수는 넣을수 없다
#예를 들면 문자와 숫자를 연결할때는 타입변환이 필요하다

#print('이 노트북의 무게는' + weight + 'kg 입니다') 라고한다면 오류가 나타난다
print('이 노트북의 무게는 ' + str(weight) + 'kg 입니다') #str을 써서 형을 변환한다
print(f"이 노트북의 무게는 {floor}kg 입니다") #혹은 f포멧 방식으로 쓸 수도 있다

#tyoe(자료형) - 자료형을 인식하는 함수
#int - 정수(integer), float - 실수 (부동) str - 문자열(string)

print(type(floor))
print(type(name))
print(round(weight))

#ag-e 13

#연습
name = 'Harin'
name = 'Jerry'
print(name)
print('***회원가입***')
user_id = 'kdt6'
user_pw = 'sf1234'
email = 'jerry@korea.com'
age = 35

print( "아이디 : ", user_id)
print( f"비밀번호 : {user_id}")
print( '이메일 : ', email)
print( '나이 : ', age)


#소수점 처리하기
n1 = 10
n2 =3
div = n1/n2
print(div)

#소수점 특정번째에서 끊어주기
print(f'결과값 : {div : .1f}') #f앞의 숫자번째까지 나타내기

#반올림 함수 -round (숫자, 자릿수)
print(round(div,3))

print(f'결과값 : {round(div,3)}')



