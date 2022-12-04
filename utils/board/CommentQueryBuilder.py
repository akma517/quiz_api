class CommentQueryBuilder:
    """
    쿼리 생성자
    """
    
     # 조회 쿼리 만들기
    def make_select_query(self, option, board_no):
        sql=""
        # 댓글 가져오기
        if option == "get":
            sql = f"""

            SELECT 
                   comment_no
                 , board_no
                 , user_id
                 , content
                 , DATE_FORMAT(insert_date, '%Y%m%d%H%i') AS insert_date
                 , DATE_FORMAT(update_date, '%Y%m%d%H%i') AS update_date
              FROM comment AS A
             WHERE board_no = {board_no}
               AND delete_yn = 'N'
             ORDER BY A.insert_date DESC

            """

        return sql
    
    
    # 수정 쿼리 만들기
    def make_update_query(self, option, comment_no=None, content=None, board_no =None ):
        sql=""
        # 댓글 수정
        if option == "modify":
            sql = f"""

            UPDATE comment
               SET content = '{content}'
             WHERE comment_no = {comment_no}

            """

        # 댓글 삭제
        elif option == "remove":
            sql = f"""

            UPDATE comment
               SET delete_yn = 'Y'
             WHERE comment_no = {comment_no}

            """
        # 댓글 일괄 삭제
        elif option == "remove_all":
            sql = f"""

            UPDATE comment
               SET delete_yn = 'Y'
             WHERE board_no = {board_no}

            """

        return sql

    # 삽입 쿼리 만들기
    def make_insert_query(self, option, user_id=None, board_no=None, content=None):
        sql=""
        # 댓글 생성
        if option == "add":
            sql = f"""

            INSERT 
              INTO comment(
                   board_no
                 , user_id
                 , content)
            VALUES ({board_no}
                 , '{user_id}'
                 , '{content}')

            """

        return sql 
