# pickle 모듈 - 객체(리스트, 딕셔너리) 형태 그래도 저장하고 읽을 수 있는 모듈
# dump - 쓰기 , load - 읽기
import pickle

with open('./output/data.txt', 'wb') as f:
    li = ['강아지', ' 닭', ' 고양이', ' 소']
    dict = { 1: '고구마', 2 : '감자', 3 : '복숭아'}
    pickle.dump(li, f) # 자료 객체, 파일 객체
    pickle.dump(dict, f) # 자료 (딕셔너리) 객체 , 파일 객체


with open('./output/data.txt', 'rb') as f2:
    # li2 = pickle.load(f)
    a = pickle.load(f2)
    b = pickle.load(f2)
    print(a)
    print(b)

print(globals())
