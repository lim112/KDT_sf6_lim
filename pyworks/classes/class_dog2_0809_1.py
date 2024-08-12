class Dog:
    tricks = []
    #클래스 변수
    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('야몽이')
dog1.add_trick('빵!')
print(dog1.tricks) #['빵!']

dog2 = Dog('참참이')
dog2.add_trick('꾹꾹이')
#클래스 변수이기 때문에 trick 2개가 다 출력됨
print(dog2.tricks) #['빵!', '꾹꾹이']

class Dog_v:
    def __init__(self, name):
        self.name = name
        self.trick = [] #지역 변수 저장, 공유 ㄴㄴ
    def add_trick(self, trick):
        self.trick.append(trick)

dog1 = Dog_v('멍멍이')
dog1.add_trick('뻥!')
print(dog1.trick) #['뻥!']

dog2 = Dog_v('설이')
dog2.add_trick('보기')
print(dog2.trick) #['뻥!']
print(dog2.trick) #['보기']