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
if __name__ == '__main__':
    c1 = Calculator(int(input('첫번째 수 ')),int(input('두번째 수 ')))
    print(f'{c1.add()} = {c1.y} + {c1.z}')
    print(f'{c1.sub()} = {c1.y} - {c1.z}')
    print(f'{c1.mul()} = {c1.y} * {c1.z}')
    print(f'{c1.div()} = {c1.y} / {c1.z}')

#0809_2 실습 3
class supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
    def print_location(self):
        #return self.location
        print(f'위치 : {self.location}')
    def change_category(self, product):
        self.product = product
        return self.product
    def show_list(self):
        print(self.product)
    def enter_customer(self):
        self.customer += 1
        return self.customer
    def show_info(self):
        print(f'위치 : {self.location}, 이름 : {self.name}, 상품 : {self.product}, 고객수 : {self.customer}')

market = supermarket('마포구','마켓온', '음료', 2)

if __name__ == '__main__':
    # '__main__'는 해당 창이라는걸 말해주는 것
    market_info = market.show_info() #위치 : 마포구, 이름 : 마켓온, 상품 : 음료, 고객수 : 2
    print(market.enter_customer()) #3
    market_customer = market.enter_customer()
    market_place = market.print_location() #위치 : 마포구
    market_product = market.show_list() #음료
    market_info = market.show_info() #위치 : 마포구, 이름 : 마켓온, 상품 : 음료, 고객수 : 4
    market_change = market.change_category('에너지바')
    print(market_change) #에너지바

class Calculator1:
    def __init__(self):
        self.value = 100
    def sub(self,value):
        self.value -= value
        return self.value
