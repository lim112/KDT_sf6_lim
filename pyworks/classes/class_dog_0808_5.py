#클래스 변수는 값을 공유하고 유지하는 속성이 있고,
#클래스 이름으로 직접 접근
class Dog:
    kind = '진돗개' #클래스 변수
    def __init__(self, name):
        self.name = name

dog1 = Dog('복숭아')
#클래스의 인스턴스 변수 만들기
print(dog1.name) #복숭아

dog2 = Dog('자두')
print(dog2.name) #자두

#클래스 변수는 클래스 이름으로 접근
print(dog2.kind) #진돗개
#사용 ㄴㄴ
print(Dog.kind) #진돗개
#위 방법말고 옆에 걸로 접근

Dog.kind = '멍개'
print(Dog.kind) #멍개

dogs = [
    Dog('멍이'), Dog('감자'), Dog('냥이')
]

for i in dogs:
    print(i.name)
