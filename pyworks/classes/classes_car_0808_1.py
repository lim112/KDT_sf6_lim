#클래스의 구성 요소 - 속성(맴버 변수), 메서드(함수)
#객체 지향 언어의 특성 : 캡슐화(추상), 정보 은닉(보안), 상속, 다형성, 첫글자는 대문자
#[생성자(매서드) : 맴버 변수, 맴버 메서드]
class Car:
    model = '' #모델명
    cc = 0
    def get_info(self): #함수 메서드
        print('모델명 :', self.model)
        print('배기량 :', self.cc)

#car_a는 메모리 힙(heap)를 사용한다
car1 = Car()
#인스턴스(객체) = 클래스 이름()
print(car1)
#objact

car1.model = '롤스로이스'
#객체.속성
print('모델명 :', car1.model) #모델명 : 롤스로이스
car1.cc = 1500
#속성 부여
print('배기량 : ', car1.cc) #배기량 :  1500
car1.get_info() #모델명 : 롤스로이스
#속성 함수 호출   #배기량 : 1500

car2 = Car()
#속성 삽입
car2.model = '캐딜락'
#속성 부여
car2.cc = 2000
car2.get_info() #모델명 : 캐딜락
#속성 함수 호출   #배기량 : 2000
