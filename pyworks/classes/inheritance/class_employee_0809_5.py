# 상속(inheritance) - 이미 구현된 클래스(부모 클래스)를 상속받아서 속성이나 기능이 확장되는 클래스(자식 클래스)
# 클래스 이름( 상속할 클래스 이름)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
p1 = Person('현수', 24)
print(p1.get_name(), p1.get_age())

class Employee(Person):
    pass        #상속 / 아래 init이 없다면 pass를 써서 받을 수 있음
    def __init__(self, name, age, id): #부모에다 자기것을 추가하고 싶다면
        super().__init__(name, age) #super()을 써서 받겠다고 선언을 해주기
        self.id = id
    def get_id(self):
        return self.id
e1 = Employee('수현', 23, 'sdf')
print('이름 :', e1.get_name() , '나이 :',e1.get_age(), '사번 :', e1.get_id())
