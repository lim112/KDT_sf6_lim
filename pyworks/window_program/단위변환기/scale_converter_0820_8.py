# 단위 변환 클래스 만들기
# KB = 1,024B, MB = 1024KB,

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        # 단위
        self.units_to = units_to
        # 변환할 단위
        self.factor = factor
        # 변환값

    def conv(self, value):
        return value/self.factor
    def __str__(self):
        return  f'{self.units_from}, {self.units_to}, {self.factor}'
if __name__ == '__main__':
# 페이지 내에서 동작시 작동
    con = ScaleConverter('KB', 'MB', 1024)
    # print(con)
    # print('1MB를 변환하기')
    # # print(str(con.convert()))
    # print(f'2{con.units_from} = {con.convert(2)}{con.units_to}') #2MB = 2048KB
    #
    # con2 = ScaleConverter('inch', 'mm', 25.4)
    # print(f'2{con2.units_from} = {con2.convert(2)}{con2.units_to}') #2inch = 50.8mm
    #
    # print(con2.__str__())
    print('***KB를 MB로 변환***')
    print(f'{con.conv(1640):.2f}{con.units_to}')