from http.client import REQUEST_URI_TOO_LONG
import pymysql
from pymysql import ROWID
import pymysql.cursors
import logging

class Database:
    """
    데이터베이스 제어
    """

    # 생성자
    def __init__(self, host, user, password, db_name, charset='utf8'):
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset
        self.db_name=db_name
        self.conn=None

    # DB 연결
    def connect(self):
        
        if self.conn != None:
            return
        
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset=self.charset
        )

    #DB 연결 해제
    def close(self):
        if self.conn is None:
            return
        if not self.conn.open:
            self.conn=None
            return
        self.conn.close()
        self.conn=None

    # SQL 실행
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
        except Exception as e:
            logging.error(e)
        finally:
            return last_row_id
    
    # 한 행 조회
    def select_one(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as e:
            logging.error(e)
        finally:
            return result

    # 전체 행 조회
    def select_all(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as e:
            logging.error(e)
        finally:
            return result
    
    # 수정 쿼리 실행
    def update(self, sql):
        cnt = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cnt = cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            logging.error(e)
        finally:
            return cnt
    
    # 삽입 쿼리 실행
    def insert(self, sql):
        cnt = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cnt = cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            logging.error(e)
        finally:
            return cnt
    
    # 삭제 쿼리 실행
    def delete(self, sql):
        cnt = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cnt = cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            logging.error(e)
        finally:
            return cnt
