# 윈도우 생성 - tkinter
# 체계 : root = tk() > Frame() > Label().Button()

# import tkinter as tk
# root = tk.Tk()

from tkinter import *
root = Tk()
root.title('처음 만든 윈도우')
# 창크기(가로*세로)
root.geometry("300x100")
# 컴포넌트(구성요소 - 레이블, 버튼, 입력상자)
# 출력
# 배치 - pack(left, right) - 한줄을 차지(TOP, BOTTOM, RIGHT, LEFT)
# grid() : 자유롭게 배치(e w s n)
Label(root, text="안녕하세요~").pack(side = BOTTOM)
Button(root, text= '확인').pack()

root.mainloop()
# 창 생성

# grid와 pack 차이점
root2 = Tk()
root2.title('두번째로 만든 윈도우')
# 창크기(가로*세로)
root2.geometry("300x200")
# 컴포넌트(구성요소 - 레이블, 버튼, 입력상자)
# 출력
# 배치 - pack(left, right) - 한줄을 차지(TOP, BOTTOM, RIGHT, LEFT)
# grid() : 자유롭게 배치(e w s n)
Label(root2, text="안녕하세요~").grid(row = 10, column = 10)
Button(root2, text= '확인').grid(row = 10 , column = 1)

root2.mainloop()
# 창 생성