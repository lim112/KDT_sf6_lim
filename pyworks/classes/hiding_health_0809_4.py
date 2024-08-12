# 정보은닉
class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp__ = 100
    def get_name(self):
        return  self.__name
    def set_hp(self, hp):
        if hp < 0:
            hp = 0
        elif hp > 100:
            hp = 100
        self.__hp__ = hp
    def get_hp(self):
        return 'hp : ' + str(self.__hp__)
    def exercise(self, hours):
        self.set_hp(self.__hp__ + hours )
        #print('술을 {}잔 마시다'.format(hours))
        print(f'술을 {hours}잔 마시다')
        # 두구문은 같은 기능이다
    def drink(self, cups):
        self.set_hp(self.__hp__ - cups)
        print('술을 {}잔 마시다'.format(cups))

p1 = Health("나몸짱")
p1.set_hp(90)
p1.exercise(3)
print(f'{p1.get_name()} - {p1.get_hp()}')

p1 = Health("한잔해")
p1.set_hp(88)
p1.exercise(4)
print(f'{p1.get_name()} - {p1.get_hp()}')

