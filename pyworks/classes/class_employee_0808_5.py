#사원의 사번을 자동 부여
class Employee:
    serial_num = 100
    def __init__(self, name):
        self.name = name
        Employee.serial_num += 1
    def __str__(self):
        #객체 정보를 출력하는 메서드
        return '사번 : {}, 이름 : {}'.format(Employee.serial_num, self.name)

emp1 = Employee('현수')
print(emp1) #현수

emp2 = Employee('수현')
print(emp2) #수현

emp3 = Employee('누나')
print(emp3) #누나