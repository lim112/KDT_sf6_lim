# 이름을 입력받아 출력하는 윈도우
from tkinter import *

def click():
    name = entry.get()
    # 입력된 이름을 가져오기
    label.config(text=name)
    # 레이블에 설정

root = Tk()
root.title('이름 입력')
# 모니터, 바라우저의 좌표 좌측상단(0,0)
root.geometry('400x400+500+200')
# 창크기 (가로 x 세로 + x좌표 + y좌표)
# 가로 세로는 생성되는 창의 크기
# 좌표는 생성되는 창의 위치

# 프레임
frame = Frame(root)
frame.pack()
# 한줄을 차지

# 컴포넌트
Label(frame, text='이름 :').grid(row = 0, column = 0)
# 입력상자(Entry())
entry = Entry(frame)
entry.grid(row = 0, column = 1)
label = Label(frame, text='')
Button(frame, text= '확인', command= click).grid(row = 1, column = 0)
label.grid(row = 2, columnspan = 2)
# columnspan 과 column의 차이점
root.mainloop()
# 창 생성