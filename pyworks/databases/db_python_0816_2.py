# 도서 관리 db
# 테이블 생성 - book
# 동적 바인딩 방식 ? 기호 사용
# db의 레코드(행)의 자료 구조는 튜플 사용, 한개일 경우 (요소,)
import sqlite3
def creat_book():
    # conn =sqlite3.connect('./output.bookdb.db')
    # 데이터 베이스 연결(db가 없다면 생성)
    conn = getconn()
    # 호출을 함수로 지정할 수 있음
    cursor = conn.cursor()
    # '작업'
    sql = """
    CREATE TABLE book(
    book_no integer primary key autoincrement,
        title text not null,
        author text not null, 
        price integer not null
    ) 
    """
    # not null 은 반드시 기입해야 하는 항목에
    cursor.execute(sql)
    conn.commit()
    # commit()은 꼭 해주기, 에러는 안나지만 '작업'이 진행되지 않음
    conn.close()
def getconn():
    conn = sqlite3.connect('./output.bookdb.db')
    return conn

def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "insert into book (title, author ,price) values(?,?,?)"
    # ?는 동적 바인딩 방식으로 기입(튜플 구조)
    cursor.execute(sql, ('점프 투 파이썬', '박응용', 19800))
    # ? 에 쓴 것을 순서대로 기입
    conn.commit()
    conn.close()
def select_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "select * from book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    conn.close()
def update_book():
    conn = getconn()
    cursor = conn.cursor()
    # '천개의 파랑'의 가격을 15000원으로 변경
    sql = "update book set price = ? where title = ?"
    cursor.execute(sql, (15000, '천개의 파랑'))
    conn.commit()
    conn.close()
def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = "select * from book where book_no = ?"
    cursor.execute(sql, (2,))
    # 동적 바인딩이 튜플로 적용되야 하기때문에 변수가 한개더라도 소괄호+ 쉼표
    rs = cursor.fetchall()
    print(rs)
    conn.close()
def delete_book():
    conn = getconn()
    cursor = conn.cursor()
    # 책 번호가 1번인 도서를 삭제
    sql = 'delete from book where book_no = ?'
    cursor.execute(sql, (1,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 다른 파일에서 임포트하기 위함
    delete_book()
    # select_one()
    # update_book()
    # creat_book()
    # insert_book()
    select_book()