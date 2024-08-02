#실습 1
#조건 - 시내 자동차의 주행속도가 50km 이상이면 "속도위반입니다"출력
#아니면 "규정속도 준수!!"

car_speed = float(input("주행속도를 입력하세요"))
if car_speed >= 50:
    print("속도 위반입니다 과태료 10만 부과")
elif car_speed < 50:
    print("규정 속도 준수!! 칭찬합니다")
print(f"주행 속도는 {car_speed}km/h 입니다")