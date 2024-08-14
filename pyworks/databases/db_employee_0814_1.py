# 사원 관리 - 조회(전체, 1건)
import sqlite3

def select_emp():
    conn = sqlite3.connect(r'C:\pydb\mydb.db')
    # db에 연결
    cur = conn.cursor()
    # 작업 객체 생성
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    # execute(문장) 문장 안에 DB Browser 에서 사용하는 언어를 써서 수정, 삭제, 조회, 생성 가능
    rs = cur.fetchall()
    # db에 있는 자료를 모두 가져오기 - 리스트로 ( rs - ResultSet)
    print(rs) # [('e101', '김사원', 3000000), ('e102', '이사원', 3500000), ('e103', '박사원', 4000000)]
    # 안에 요소가 튜플로 출력
    conn.close()
    print(rs[0])
    print(rs[-1])

    for i in rs:
        print(i)

def insert_emp():
    conn = sqlite3.connect(r'C:\pydb\mydb.db')
    cur = conn.cursor()
    # sql = "INSERT INTO employee VALUES ('e105', '조대리', 4500000)"
    sql = "INSERT INTO employee VALUES ('e107', '정신입', 0)"
    cur.execute(sql)
    conn.commit()
    # 자료 삽입, 수정, 삭제 후에는 반드시 commit() 명시, commit()의 빠져버리면 실행자체가 안됨
    conn.close()
# 이미 들어갔는데 또 실행하면 에러
# DB browser 를 닫고 실행하기 열고 실행하면 에러


def update_emp():
    conn = sqlite3.connect(r'C:\pydb\mydb.db')
    cur = conn.cursor()
    # 고신입의 급여를 2500000으로 수정
    sql = "UPDATE employee SET name = '박대리' WHERE name = '박사원'"
    cur.execute(sql)
    conn.commit()
    conn.close()

def delete_emp():
    conn = sqlite3.connect(r'C:\pydb\mydb.db')
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = '이사원'"
    # 이름이 이사원인 사람 정보 삭제
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_one():
    conn = sqlite3.connect(r'C:\pydb\mydb.db')
    cur = conn.cursor()
    sql = "SELECT*FROM employee WHERE name LIKE '%신입%'"
    # 이름에 사원이 들어가는 사람의 정보 출력
    cur.execute(sql)
    #rs = cur.fetchall()
    # 튜플로 출력
    rs = cur.fetchone()
    # 튜플이 아니라 리스트로 출력
    print(rs)
    conn.close()


select_emp()
# insert_emp()
# update_emp()
# delete_emp()
select_one()
