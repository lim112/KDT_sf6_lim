# 달력 모듈
import calendar as cal
import datetime as dt

# 2024년 달력
# cal.prcal(2024)

# 2024년 8월
cal.prmonth(2024, 8)

# 2024년 8월 12일 요일
# 월 : 0, 토 - 6
#print(cal.weekday(2024, 8, 12))

# 숫자 인덱스를 용리로 바꾸기
days = [
    '월', '화', '수', '목', '금', '토', '일'
]

print(days[0]) #0

# 오늘의 요일
weekday = dt.date.today().weekday()
print(weekday)
print(f'오늘은 {days[weekday]}요일') # 오늘은 월요일

day815 = dt.date(2024,8,15).weekday()
print(f'광복절은 {days[day815]}요일 입니다') # 광복절은 목요일 입니다

#날짜를 입력하면 요일을 출력하는 함수 정의
def get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    idx = dt.date(yyyy, mm, dd).weekday()
    print('{}년 {}월 {}일 {}요일'.format(yyyy,mm, dd, days[idx])) # 2024년 8월 15일 목요일
    # 다른 버전
    print(f'{yyyy}년 {mm}월 {dd}일 {days[idx]}요일') # 2024년 8월 15일 목요일

get_weekday( 2024, 8, 15)

# 9월 달력
cal.prmonth(2024,9)