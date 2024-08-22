from tkinter import *
# 체계 : root = Tk() > Frame() > Label(),Button() > mainloop()

def click():
    Label.config(text="안녕 파이썬")

# 루트
root = Tk()
root.title('윈도우 3')

# 창크기(가로*세로)
root.geometry("300x200")
root.option_add('*Font', '돋움 15')
# 프레임
frame = Frame(root)
frame.pack()
# 무슨 의미?

Label(frame, text="hello ~python").grid(row = 0, column = 0)
Button(frame, text= '확인').grid(row = 1 , column = 0)
# label, button 안에 root, frame이 들어가는 차이
label = Label(frame, text='')
label.grid(row = 2, column = 0)

root.mainloop()
# 창 생성
