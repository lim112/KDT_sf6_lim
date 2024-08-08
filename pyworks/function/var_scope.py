# 변수의 유효범위
# 전역 - 전체에 영향을 미침
# 지역 - 함수나 제어문(if,반복문)내에서 영향을 미친다, 빠져나오면 소멸한다

# 상품 가격 = 단위당 가격 + 수량
'''quantity = 2
def get_price():
    price = 4000 * quantity
    return price

order_price = get_price()
print(f'{quantity}개에  {order_price}원 입니다')


def one_up():
    x = 0
    x += 1
    return x
print(one_up())
print(one_up())

products = [[30000, 15000]]
def product_price():
    for i in products:
        if i < 20000:
            delivery = i + 2500
            print('상품 1 가격 :', delivery)
        else:
            delivery = i
            print('상품 2 가격 :', delivery)

product_price()'''

def order_product(product, count):
    if product * count < 20000 :
        return product * count + 2500
    else :
        return product * count
price1 = order_product(int(input("상품 1 가격을 입력해주세요 ")), int(input('상품의 수량을 입력해주세요 ')))
price2 = order_product(int(input("상품 2 가격을 입력해주세요 ")), int(input('상품의 수량을 입력해주세요 ')))
print(f'상품1 가격 : {format(price1, ',d')}원')
print(f'상품2 가격 : {format(price2, ',d')}원')

