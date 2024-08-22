from tkinter import *

def click():
    result = value.get()
    text.delete(0.0, END)
    text.insert(END, result)

root = Tk()
root.geometry('200x100')
root.title('정수형 변수')

# 정수형 객체 선언 - 객체 : 클래스이기 때문에
value = IntVar()
value.set(10)

Button(root, text='확인', command=click).grid(row = 0, column = 0)

text = Text(root, width=2, height=1)
text
root.mainloop()
