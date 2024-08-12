# 카운터 만들기 - 클래스 변수
class Counter:
    x = 0
    def __init__(self):
        Counter.x += 1

c1 = Counter()
print(Counter.x) #1
c2 = Counter()
print(Counter.x) #2
c3 = Counter()
print(Counter.x) #3

# 인스턴스 변수와 클래스 변수 차이
# 인스턴스 변수는 저장되지 않고, 클래스 변수는 저장된다
class Counter2:
    def __init__(self):
        self.x = 0
    def plus(self):
        self.x += 1
        return self.x
count1 = Counter2()
print(count1.plus()) #1
count2 = Counter2()
print(count2.plus()) #1
count3 = Counter2()
print(count3.plus()) #1
