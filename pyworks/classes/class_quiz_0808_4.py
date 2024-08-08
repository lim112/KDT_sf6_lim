# 실습 1 - 사칙 연산 클래스 만들기
import sys
class Calculator:
    def __init__(self,y,z):
        self.y = y
        self.z = z
    def add(self):
        return self.y + self.z
    def sub(self):
        return self.y - self.z
    def mul(self):
        return self.y * self.z
    def div(self):
        if self.y != 0:
            return self.y / self.z

        else:
            print('0으로 나눌수 없습니다')
            return sys.exit() #바로 나가게 만드는

c1 = Calculator(int(input('첫번째 수 ')),int(input('두번째 수 ')))
print(f'{c1.add()} = {c1.y} + {c1.z}')
print(f'{c1.sub()} = {c1.y} - {c1.z}')
print(f'{c1.mul()} = {c1.y} * {c1.z}')
print(f'{c1.div()} = {c1.y} / {c1.z}')
