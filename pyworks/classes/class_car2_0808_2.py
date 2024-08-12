# 생성자(constructor)
class Car:
    def __init__(self, models, year):
        #생성자를 만들때 classes_car가 직접적이라면
        #이건 간접적 model등 항목에 직접 접근하지 않는다
        #(클래스 밖에서 접근하지 않으니)
        self.model = models
        #초기화
        self.year = year
        #초기화

    def show_info(self):
        print(f'모델명 : {self.model}, 연식 : {self.year}')

#car_a는 메모리 힙(heap)를 사용한다
car_a = Car('테슬라s', 2023)
#캡슐화
car_a.show_info()

car_b = Car('팬텀', 2020)
car_b.show_info()

#객체 리스트 만들기
cars = [
    Car('팬텀', 2020), Car('머스탱', 1969), Car('소나타', 2023)
]

car_c = Car('g90', 2023)
print(car_c.show_info())
#cars[0].show_info()
for i in cars:
    i.show_info()

print(cars[0]) #<__main__.Car object at 0x000001EAE1A420F0>
                    # 0x000001EAE1A420F0는 메모리의 주소가 된다