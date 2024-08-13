with open('./source/city.txt', 'r') as f:
     # data = f.readlines()
     a = []
     # 2차원 리스트 만들기
     for i in range(6):
         data = f.readline().split()
         # 구분 기호로 분리한뒤 리스트로 만들기 (공백을 구분 기호)
         a.append(data)
     print(a) # [['서울'], ['인천'], ['부산'], ['광주'], ['대전'], ['대구']]
     # 각 항목들도 리스트에 담기

     # 리스트위 요소 출력
     print(a[0]) # ['서울']
     print(a[-1]) #['대구']
     print(a[0][0]) # 서울
     for i in a:
        print(i)
