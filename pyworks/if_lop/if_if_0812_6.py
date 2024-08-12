# if ~ if 구문과 if ~ elif 구문의 차이
# elif 는 참인 해당 구문만 실행됨
# if ~ if 는 참인 값은 모두 실행됨
str = 'life is short, you need python'

# if 'Wife' in str:
#     print('Wife')
# elif 'Life'in str and 'Python' not in str:
#     print('Life')
# elif 'good' not in str:
#     print('good')
# elif 'need' in str:
#     print('need')
# else:
#     print('none')

if 'Wife' in str:
    print('Wife')
elif 'Life'in str and 'Python' not in str:
    print('Life')
elif 'good' not in str:
    print('good')
elif 'need' in str:
    print('need')
else:
    print('none')
