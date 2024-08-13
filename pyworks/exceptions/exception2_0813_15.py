# try ~ except ~ finally
def divide(x, y):
    try:
        # 실행되는 구간(예외가 발생할 수 있음)
        result = x/ y
        print(result)
    except ZeroDivisionError:
        # 예외 처리 구간
        print('0으로 나눌 수 없습니다')
    finally:
        # 실행의 성공 여부 상관 없이 실행되는 구문
        print('여기는 반드시 수행됩니다')

divide(3,2) # 1.5
                  # 여기는 반드시 수행됩니다