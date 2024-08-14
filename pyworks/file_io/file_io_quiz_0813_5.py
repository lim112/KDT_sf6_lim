# # 실습 1 - 구구단 전체를 파일로 저장
# f = open(r'C:\pyfile\gugudan.txt','w' )
# gugudans = []
#
# for i in range(2, 10):
#     # 몇단?
#     for j in range(1, 10):
#         # 몇을 곱해?
#         gugu = i * j
#         f.write(f'{i} x {j} = {gugu} \n')
#     f.write('\n')
#     # 줄바꿈
# f.close()
#
# f =  open(r'C:\pyfile\gugudan.txt','r' )
# print(f.read())
# f.close()

# 실습 2
user_list = ''
try:
    with open('./source/member.txt', 'w') as f:
        users = [('김기용', 'jerry123'), ('이정훈', 'luna'), ('정윤아', 'rena')]
        for i in users:
            f.write(f'{i[0]} {i[1]} \n')
        f.close()
    with open('./source/member.txt', 'r') as f2:
        user_list = []
        user_list = f2.read()
        print(user_list)
except:
    print('파일을 찾을 수 없음')
print(user_list[-1])
# 실습 3
# try:
#     with open('./source/member.txt', 'r') as f2:
#         user_list = f2.read()
#         print(user_list)
#         user_check = input('이름을 입력하세요 :')
#         pw_check = input('비밀번호를 입력하세요 :')
#         for i in
#             if
