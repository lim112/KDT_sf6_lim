from tkinter import *
dic = {
    '비트' : '0 이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위\n',
    '변수' : '어떤 1개의 자료를 저장하기 위해 메모리 할당 공간\n',
    '리스트' : '여러 개의 연속적인 자료를 저장하는 자료구조\n'
}


root = Tk()
def click():
    try:
        word = entry.get()
        definition = dic[word]
        # dic[word] # dic[key] > value
        text.delete(0.0, END)
        # 0행의 0번 글자부터 마지막까지 지우기
        text.insert(END, definition) # end - 최종 입력지점
        text.insert(END, definition)
    except KeyError:
        definition = "단어를 찾을수 없습니다"
    text.insert(END, definition)
        # 마지막 부분에 결과값 입력
        # print를 쑬 수는 없어서


root.title('컴퓨터 소사전')
Label(root, text='안어를 입력하고 제출 버튼을 누르세요').grid(row = 0, column = 0)
entry = Entry(root)
entry.grid(row = 1, column = 0, sticky = W)
Button(root, text= '제출', command= click).grid(row = 2, column = 0, stick = W)

# 프레임
frame = Frame(root)
frame.grid()
# 출력 상자 - Text()
text= Text(root, width=80, height=10, bg = 'green')
text.grid(row  = 3, column = 0, sticky = W )

root.mainloop()