from tkinter import *

def convert():
    kb = int(entry_kb.get())
    mb = kb / 1024
    mb = f'{mb : .2f}'
    text_mb.delete(0.0, END)
    # 이전것 지우기
    text_mb.insert(END, mb)

root = Tk()
root.title("단위 변환기")
root.geometry("250x100+200+200")
entry_kb = Entry(root)
# 입력 필드 추가 (킬로바이트), Entry() - 입력 상자
Label(root, text="킬로바이트 (KB):").grid(row=0, column=0, padx=10, pady=5)
entry_kb.grid(row=0, column=1, padx=10, pady=5)

# 변환 결과를 표시할 필드 추가 (메가바이트)
Label(root, text="메가바이트 (MB):").grid(row=1, column=0, padx=10, pady=5)

text_mb = Text(root, width=20, height=1)
        # Text() - 출력 클래스 컴포넌트
text_mb.grid(row=1, column=1, padx=10, pady=5)

# 변환 버튼 추가
Button(root, text="변환", command=convert).grid(row=2, column=1, padx=10, pady=5)
root.mainloop()


