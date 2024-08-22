# 쿠폰 추첨기
# 추첨 버튼을 누르면 3명이 랜덤하게  출력됨
import random
from tkinter import *
name_choice = []
def click():
    global name_choice
    namelist = [
    '김용준', '김용혁','임현수', '윤종관', '정지은', '오민선', '최준영',
        '윤다빈', '박민우', '조형주', '고지수'
    ]
    name_choice = set()
    while len(name_choice) < 3:
        name = random.choice(namelist)
        name_choice.add(name)

    # name_choice = random.choices(namelist, k=3)
    text.delete(0.0, END)
    text.insert(1.0, name_choice)
window = Tk()
window.title("쿠폰 추첨기")

# 이미지 넣기
lbl_img = Label(window)

# 이미지 객체 생성
img = PhotoImage(file='bronx.png')

# 이미지 넣기
lbl_img.config(image=img)
lbl_img.grid(row=0, column = 0, sticky=W)

# 추첨 버튼
Button(window, text="추첨", command=click).grid(row = 1,column =1,sticky = E)

# 출력상자
text = Text(window,width=50, height=3, bg='yellow')
text.grid(row=2,column=0,sticky =W)

window.mainloop()
