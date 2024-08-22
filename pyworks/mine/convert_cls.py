# # 클래스로 단위 변환 샘플
# from tkinter import *
from window_program.단위변환기.scale_converter_0820_8 import ScaleConverter
from tkinter import *

class App(ScaleConverter):
    def __init__(self, root):
        self.conv = ScaleConverter('KB',"MB","1024")
        frame = Frame(root)
        frame.pack()

        # 한줄을 꽉 채움( 가운데 정렬)
        Label(frame, text="KB").grid(row = 0, column = 0)
        self.kb = IntVar()
        # textvariable : 객체(맴버) 변수 "kb'입력

        Entry(frame, textvariable=self.kb).grid(row = 0, column = 0)
        Label(frame, text="MB").grid(row = 1, colunm = 0)
        # entry로 출력 kb

        # 'mb' 출력
        self.mb = DoubleVar()
        # DoubleVar : 실수형 객체
        Label(frame, textvariable=self.mb).grid(row = 2, column =2)

        Button(frame, text="변환", command=self.convert).grid(row=1, columnspan=0)
        # 버튼 생성시 아니라 버튼 동작시 작동

    def convert(self):
        print('구현 ㄴ')

    pass

root = Tk()
root.title('단위 변환기')
root.geometry('300x200+200+200')

app = App(root)
# root를 인자로 생성

root.mainloop()