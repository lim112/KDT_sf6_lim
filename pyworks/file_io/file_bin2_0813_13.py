# 이미지 파일 읽고 쓰기
with open('horse-6290422_640.jpg', 'rb') as f1:
    img = f1.read()
    # 복사

with open('./output/horse-6290422_640.jpg', 'wb') as f2:
    f2.write(img)
    # 붙혀넣기
