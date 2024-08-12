class Calculator:
    def __init__(self):
        self.x = 0 #맴버변수, 인스턴스 변수 (지역변수)
    def add(self, y):
        self.x += y
        return self.x
    def sub(self, y):
        self.x -= y
        return self.x
c1 = Calculator()
print(c1.x)
print(c1.add(10)) #10 더하기
print(c1.sub(3)) #7

print(c1.x)
for i in range(3):
    if c1.x > 6:
        print(c1.x) #'7' 출력, c1.x는 전역변수로 저장되는걸까? ㄴㄴ 맴버 변수

c2 = Calculator()
print(c2.x)
print(c2.add(20)) #10 더하기
print(c2.sub(5)) #15

#print(globals())

