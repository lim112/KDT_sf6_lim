from classes.class_quiz_0808_4 import Calculator1

class LimitCalculator(Calculator1):
    def sub(self,value):
        if self.value < 0:
            self.value = 0
            #super().sub(value)
            #다른 방법
        return self.value

lc = LimitCalculator()
print(lc.sub(20)) #80
print(lc.sub(90)) #0