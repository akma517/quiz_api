from utils.Database import *
from config.DatabaseConfig import *

class QueryExecuter:
    def __init__(self):
        self.db = Database(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db_name=DB_NAME,
        )
    
    # 쿼리 실행 함수를 전달 받아 db 연결 -> 실행 -> db 연결 해제 -> 결과 리턴
    def excuteQuery(self, excuteFunc, sql):
        result = None
        try:
            self.db.connect()
            result = excuteFunc(sql)

        except Exception as e:
            print(e)

        finally:
            if self.db is not None:
                self.db.close()
        return result
        
    # 퀴즈 문제 가져오기
    def get_questions(self, sql):
        questions = self.excuteQuery(excuteFunc = self.db.select_all, sql = sql)
        return questions

    # 퀴즈 메타 가져오기
    def get_quiz_metas(self, sql):
        quiz_metas = self.excuteQuery(excuteFunc = self.db.select_all, sql = sql)
        return quiz_metas

    # 회원 가져오기
    def get_user(self, sql):
        user = self.excuteQuery(excuteFunc = self.db.select_all, sql = sql)
        return user
        
    # 로그인 로그 넣기
    def add_user_history(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.insert , sql = sql)
        return cnt

    # 비밀번호 변경하기
    def modify_user_password(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 시험이력 넣기
    def add_test_hisotory(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.insert , sql = sql)
        return cnt
    
    # 시험이력 가져오기
    def get_test_history(self, sql):
        user = self.excuteQuery(excuteFunc = self.db.select_all, sql = sql)
        return user 
    
     # 시험이력 논리적 삭제
    def remove_test_hisotory(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt
    
    # 북마크 추가
    def add_bookmark(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.insert , sql = sql)
        return cnt

    # 북마크 논리적 삭제
    def remove_bookmark(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 북마크 논리적 추가
    def add_bookmark(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 북마크 기존재여부 확인
    def get_bookmark(self, sql):
        exist = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return exist
    
    # 북마크 가져오기
    def get_bookmarks(self, sql):
        bookmarks = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return bookmarks

    # 구독상품 가져오기
    def get_subscribe_products(self, sql):
        subcribe_products = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return subcribe_products

    # 구독상태 가져오기
    def get_subscribe(self, sql):
        subcribe = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return subcribe

    # 게시글 가져오기
    def get_boardlist(self, sql):
        boardList = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return boardList

    # 게시글 수정하기
    def modify_board(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 게시글 논리적 삭제
    def remove_board(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 게시글 생성하기
    def add_board(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.insert , sql = sql)
        return cnt

    # 댓글 가져오기
    def get_comments(self, sql):
        comments = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return comments

    # 댓글 수정하기
    def modify_comment(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 댓글 논리적 삭제
    def remove_comment(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt
    
    # 댓글 논리적 일괄 삭제
    def remove_all_comment(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.update , sql = sql)
        return cnt

    # 댓글 생성하기
    def add_comment(self, sql):
        cnt = self.excuteQuery(excuteFunc = self.db.insert , sql = sql)
        return cnt     


    # 로그인로그 가져오기
    def get_logins(self, sql):
        log = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return log

    # 로그인횟수 가져오기
    def get_logins_cnt(self, sql):
        log = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return log

    # 시험이력로그 가져오기
    def get_tests(self, sql):
        log = self.excuteQuery(excuteFunc = self.db.select_all , sql = sql)
        return log
    