# 클래스의 상속 - 매서드 재정의 (오버라이딩)
class Airplane:
    def __init__(self): # 기본 생성자, init 메서드를 생략해도 기본적으로 작동 함
        print('비행기의 클래스가 생성되었습니다')
    def take_off(self):
        print('비행기가 이륙합니다')
    def fry(self):
        print('비행기가 일반 비행합니다')

    def land(self):
        print('비행기가 착륙합니다')

air1 = Airplane() #비행기의 클래스가 생성되었습니다
air1.take_off() #비행기가 이륙합니다
air1.fry() #비행기가 일반 비행합니다
air1.land() #비행기가 착륙합니다

class SuperSonicAirplane(Airplane):
    # 1 - nomal, 2 - supersonic
    NORMAL = 1 # 클래스 상수 ( 대문자 관례 )
    SUPERSONIC = 2

    # 맴버 변수 선언 - 비행 모드
    def __init__(self):
        self.fry_mode = SuperSonicAirplane.NORMAL # 초기 설정

    def fry(self):
        if self.fry_mode == SuperSonicAirplane.SUPERSONIC: # 설정 변경
            print('비행기가 초음속 비행합니다')
        else:
            super().fry() # 메서드 상속때도 super()

            #print('비행기가 일반 비행합니다')

f22 = SuperSonicAirplane() # 객체(인스턴스) 생성
f22.take_off() #비행기가 이륙합니다
f22.fry() #비행기가 일반 비행합니다
f22.fry_mode = SuperSonicAirplane.SUPERSONIC
f22.fry() #비행기가 초음속 비행합니다
f22.land() #비행기가 착륙합니다