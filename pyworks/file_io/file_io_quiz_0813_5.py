# # # 실습 1 - 구구단 전체를 파일로 저장
# # f = open(r'C:\pyfile\gugudan.txt','w' )
# # gugudans = []
# #
# # for i in range(2, 10):
# #     # 몇단?
# #     for j in range(1, 10):
# #         # 몇을 곱해?
# #         gugu = i * j
# #         f.write(f'{i} x {j} = {gugu} \n')
# #     f.write('\n')
# #     # 줄바꿈
# # f.close()
# #
# # f =  open(r'C:\pyfile\gugudan.txt','r' )
# # print(f.read())
# # f.close()
#
# # 실습 2
# user_list = []
# try:
#     with open('./source/member.txt', 'w') as f:
#         user_names = ('김기용', '이정훈', '정윤아')
#         user_pws = ('jerry123', 'luna', 'rena')
#         # user_list = [user_names, user_pws]
#         # print(user_list)
#         for i in user_names:
#             f.write(f'{i} \n')
#         for i in user_pws:
#             f.write(f'{i} \n')
#         f.close()
#     with open('./source/member.txt', 'r') as f2:
#         user_list = []
#         user_list = f2.read()
#
#         # user_check = input('이름을 입력하세요')
#         # pw_check = input('비밀번호를 입력하세요')
#         # for i in range(4):
#         #     pass
#         print(user_list[0])
# except:
#     print('파일을 찾을 수 없음')
# print(user_list[-1])
# # 실습 3
# name = input('이름을 입력하세요')
# pw = input('비밀번호를 입력하세요')
# user = name + ' ' + pw
# with open('./source/member.txt', 'r')as f:
#     member_list = f.readlines()
#     print(member_list)
#     # 상태변수 - true/fale
#     sw = False
#     for member in member_list:
#         # 리ㅣ스트를 순화하면서
#         if member == user:
#             # 파일에 있는 name, pw와 입력한 유저의 name, pw가 일치하면
#             sw = True
#             # 상태를 True로 저장
#     if sw == True:
#         # sw만써도 같은 의미
#         print('로그인 성공!!')
#     else:
#         print('로그인 실패!!')
# # 내가 만들기
# # try:
# #     with open('./source/member.txt', 'r') as f2:
# #         user_list = f2.read()
# #         print(user_list)
# #         user_check = input('이름을 입력하세요 :')
# #         pw_check = input('비밀번호를 입력하세요 :')
# #         for i in
# #             if
# 실습 2(실습 3과 연결됨)
'''
try:
    with open("source/member.txt", "w") as f:
        for i in range(3):
            name = input("이름을 입력하세요: ")
            pw = input("비밀번호를 입력하세요: ")
            f.write(f'{name} {pw}\n')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
'''

try:
    with open("./source/member.txt", "r") as f:
        member = f.read()
        print(member)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 실습 3
# 로그인
name = input('이름 입력: ')
pw = input('비밀번호 입력: ')
user = name + " " + pw + "\n"

with open("./source/member.txt", "r") as f:
    member_list = f.readlines()  # 데이터를 리스트로 반환
    # print(member_list)
    print(member_list)
    # 상태 변수 - True/Fasle
    sw = False  # 상태 초기화 False임
    for member in member_list: #리스트를 순회하면서
        # 파일에 있는 member의 name, pw와 입력한 user의 name, pw가 일치하면
        if member == user:
            sw = True  #상태를 True로 저장

    if sw == True :  #sw == True
        print("로그인 성공!")
    else:  #sw == False
        print("로그인 실패!")