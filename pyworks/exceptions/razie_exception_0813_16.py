# rasie exception - 예외 미루기
# 예외 처리를 미루면 호출하는 쪽에서 예외 처리

class Animal:
    def breathe(self):
        print('숨을 쉰다')
    def cry(self):
        # 메서드를 구현하지 않고 미뤄둠
        raise NotImplementedError
        # 나중에 상속받을때는 반드시 부여 할 것

class Dog(Animal):
    def sleep(self):
        print('강아지가 잠을 잔다')
    def cry(self):
        print('왈 멍')


dog = Dog()
dog.breathe() # 숨을 쉰다
dog.sleep() # 강아지가 잠을 잔다
dog.cry() # 왈 멍
# NotImplementedError 자식 클래스에서 cry 함수를 재정의 하지않고 호출하면 에러 발생

class Cat(Animal):
    def sleep(self):
        print('고양이가 잠을 잡니다')
    def cry(self):
        print('야용')
cat = Cat()
cat.sleep() # 고양이가 잠을 잡니다
cat.cry() # 야용

