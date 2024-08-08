#클래스 변수는 값을 공유하고 유지하는 속성이 있고,
#클래스 이름으로 직접 접근
class Dog:
    kind = '진돗개' #클래스 변수
    def __init__(self, name):
        self.name = name

dog1 = Dog('복숭아')
print(dog1.name)

dog2 = Dog('자두')
print(dog2.name)

#클래스 변수는 클래스 이름으로 접근
print(dog2.kind) #사용 ㄴㄴ
print(Dog.kind) #위 방법말고 옆에걸로 접근

Dog.kind = '멍개'
print(Dog.kind)
