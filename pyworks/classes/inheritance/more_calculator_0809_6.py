# 모듈(module) 불러오기
import sys

from classes.class_quiz_0808_4 import Calculator
calc = Calculator(5,4)
print(calc.add())
print(calc.div())
print(calc.sub())
print(calc.mul())

class MoreCalculator(Calculator):
    def pow(self):

        return self.y ** self.z

    def div(self): # 부모 클래스와 메서드 이름을 같게 한다면 불러오기
                    #다르게 한다면 새로 만들기
        try:
            return self.y / self.z # 부모의 매개변수와 같은걸로
        except:
            print('0으로 나눌수 없습니다')
            sys.exit(0)

mc = MoreCalculator(6,2)
print(mc.add())
print(mc.pow())