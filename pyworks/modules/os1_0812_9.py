# os 모듈 - 디렉토리, 파일 등의 자원을 제어하는 모듈
import os
file_path = os.chdir("C:/KDT_SF6/pyworks/modules")
file_path = os.chdir(r"C:\KDT_SF6\pyworks\modules")
file_path = os.chdir("C:\\KDT_SF6\\pyworks\\modules")
# 위는 다 같은 뜻이다
dir = os.popen('dir')
                # dir명령으로 열기 - 목록보기
print(dir.read())
print(os.listdir(file_path)) # ['calendar1_0812_5.py', 'datetime1_0812_4.py', 'game', 'math1_0812_3.py', 'modul_quiz_0812_7,0813_8.py', 'mylib_0812_10', 'os1_0812_9.py', 'random1_0812_6.py', 'sys1_0812_8.py', 'time1_0812_12.py', 'use_mylib_0812_11.py']
# 파일들 이름을 리스트로 저장


