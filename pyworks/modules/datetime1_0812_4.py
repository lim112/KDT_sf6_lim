import datetime
# 날짜와 시간 모두 출력
now = datetime.datetime.today()
print(now) # 2024-08-12 16:05:43.369411

print(now.year) # 2024
print(now.month) # 8
print(now.day) # 12
print(now.second) # 35

#날짜만 출력
print(f'{now.year} - {now.month} - {now.day} ') # 2024 - 8 - 12

#시간만 출력
print(f'{now.hour}:{now.minute} : {now.second}') # 16:15 : 46

#2024년 7월 31일 출력
the_day = datetime.date(2024,7,31)
print(the_day) # 2024-07-31

#오늘 날짜만 출력
today = datetime.date.today()
print(today) # 2024-08-12
print('🏀 지금까지 며칠? 🏀') # 🏀 지금까지 며칠? 🏀
passed_time = today - the_day
print(passed_time) # 12 days, 0:00:00
print(f'개강 이후{passed_time}일 지났습니다.') # 개강 이후12 days, 0:00:00일 지났습니다.

#추석까지 며칠 남았나?
the_day = datetime.date(2024, 9, 17)
D_day = the_day - today
print(f'추석까지 {D_day}남았습니다') # 추석까지 36 days, 0:00:00남았습니다
print(f'추석까지 {D_day.days}일 남았습니다') # 추석까지 36일 남았습니다
                    #days : 날짜만 남도록 출력




