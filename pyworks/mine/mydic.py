from tkinter import *

# 사전 데이터
dic = {
    '비트': '0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위',
    '변수': '어떤 1개의 자료를 저장하기 위해 메모리 할당 공간',
    '리스트': '여러 개의 연속적인 자료를 저장하는 자료구조'
}

root = Tk()

def click():
    word = entry.get()  # 입력된 단어를 가져옴
    meaning = dic.get(word, "정의된 단어가 없습니다.")  # 단어의 뜻을 가져오거나 없으면 메시지 출력
    text.insert(END, f"{word}: {meaning}\n")  # 텍스트 박스에 출력

root.title('컴퓨터 소사전')

# 라벨과 입력 필드
Label(root, text='단어를 입력하고 제출 버튼을 누르세요').grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=1, column=0, sticky=W)

# 제출 버튼
Button(root, text='제출', command=click).grid(row=2, column=0, sticky=W)

# 출력 상자 - Text()
text = Text(root, width=80, height=10, bg='green')
text.grid(row=3, column=0, sticky=W)

root.mainloop()
