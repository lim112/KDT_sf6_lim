#정보 은닉(보안 유지하기 위해 접근을 허용하지 않음)
#접근 제어자 - public, private, protected(실제로 사용하지는 않고 숨겨져 있다)
#외부로 쓰지 않고 내부적으로 작동함

class Person:
    def __init__(self, name):
        self.__name__ = name
        #언더바를 넣으면 클래스 밖에서 접근할때 자동입력이 되지 않음
        #> 외부에서 접근할 수 없다 따라서 함수로 이름 입력하기 추가
        self.age = 0
    #get, set 매서드(함수)를 만들어서 조회, 수정하기
    #get = 조회(출력), set = 입력(수정)
    def set_name(self, name):
        self.__name__ = name
    def get_name(self):
        return self.__name__
    def set_age(self, age):
        self.age = age
    def get_age(self):
        print(self.age)

p1 = Person('수현')
p1.set_name('현수')
p1 = Person('수현')

print(p1.get_name())
p1.set_age(21)
print(p1.get_age())