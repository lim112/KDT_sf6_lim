# 클래스로 단위 변환 샘플
from tkinter import *
from scale_converter_0820_8 import *
class App(ScaleConverter):
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        # 한줄을 꽉 채움( 가운데 정렬)
        Label(frame, text="KB").grid(row = 0, column = 0)
        Button(frame, text = "변환", command = self.convert).grid(row = 1, column = 0)
                                                    # 버튼 생성시 아니라 버튼 동작시 작동
    def convert(self):
        print('구현 ㄴ')
        
    pass

root = Tk()
root.geometry('300x200+200+200')
root.title('단위 변환기')
app = App(root)
# root를 인자로 생성
root.mainloop()
