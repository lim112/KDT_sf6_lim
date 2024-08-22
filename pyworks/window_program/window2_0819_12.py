from tkinter import *

# grid와 pack 차이점
root2 = Tk()
root2.title('두번째로 만든 윈도우')
# 창크기(가로*세로)
root2.geometry("300x200")
# 컴포넌트(구성요소 - 레이블, 버튼, 입력상자)
# 출력
# 배치 - pack(left, right) - 한줄을 차지(TOP, BOTTOM, RIGHT, LEFT)
# grid() : 자유롭게 배치(e w s n)
Label(root2, text="안녕하세요~").grid(row = 0, column = 0)
Button(root2, text= '확인').grid(row = 1 , column = 1, sticky = E)

root2.mainloop()
# 창 생성