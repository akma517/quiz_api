class BookmarkQueryBuilder:
    """
    쿼리 생성자
    """

    def make_select_query(self, option, user_id, quiz_no=None, question_no=None):
        sql=""
        # 북마크가 이미 존재하는지 확인
        if option == "exist":
            sql = f"""

            SELECT 
                   COUNT(question_no) AS exist
              FROM bookmarks
             WHERE question_no = {question_no}
               AND user_id = '{user_id}'
               AND quiz_no = {quiz_no}

            """
        elif option == "get":
            sql = f"""

            SELECT 
                   quiz_no
                 , quiz_name
                 , image_path       
              FROM quiz_meta AS A
             WHERE EXISTS(SELECT 
                                 B.quiz_no 
                            FROM bookmarks AS B 
                           WHERE B.user_id='{user_id}' 
                             AND B.quiz_no = A.quiz_no
                             AND B.delete_yn = 'N')
            """
        return sql
    
    # 수정 쿼리 만들기
    def make_update_query(self, option, user_id, quiz_no, question_no):
        sql=""

        # 논리적 삭제
        if option == "remove":
            sql = f"""

            UPDATE bookmarks
               SET delete_yn = 'Y'
             WHERE question_no = {question_no}
               AND user_id = '{user_id}'
               AND quiz_no = {quiz_no}
            
            """
        
        # 논리적 추가
        elif option == "add":
            sql = f"""

            UPDATE bookmarks
               SET delete_yn = 'N'
             WHERE question_no = {question_no}
               AND user_id = '{user_id}'
               AND quiz_no = {quiz_no}
            
            """

        return sql 

    # 삽입 쿼리 만들기
    def make_insert_query(self, option, user_id, quiz_no, question_no):
        sql=""

        # 북마크 추가
        if option == "add":
            sql = f"""
            
            INSERT 
              INTO bookmarks(
                   user_id
				 , quiz_no
				 , question_no)
            VALUES ('{user_id}'
				 , {quiz_no}
			     , {question_no})
            
            """
   
        return sql 






