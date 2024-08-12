# 단위 변환기 확장 클래스
# 클래스의 상속 기능 구현
# F(화씨) = C(섭씨) * 1.8 +32
from classes.class_scale_converter_0812_1 import ScaleConverter
            # 파일을 불러올 수도 있음
class Converter(ScaleConverter):
    # 자식 클래스(부모 클래스):
    def __init__(self, units_from, units_to, factor, offset):
        self.offset = offset
        # 자식의 맴버 변수
        super().__init__(units_from, units_to, factor)
        # 부모의 맴버 변수
    def __str__(self):
    #   return f'{super().__str__()}, {self.offset}'
    #   다른 방식
        return f'{self.units_from}, {self.units_to}, {self.factor}, {self.offset}'
    def convert(self, value):
        return value * self.factor + self.offset

con = Converter('C','f',1.8, 32)
print(con)
print(f'33{con.units_from} = {con.convert(33)}{con.units_to}')