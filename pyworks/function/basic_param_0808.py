#기본 매개변수
#함수 호출시 매개변수를 생략하면 기본값이 대입됨
def pr_str(txt, count = 3):
    for i in range(count):
        print(txt)

pr_str('hello~')