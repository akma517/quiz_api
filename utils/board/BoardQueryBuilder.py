class BoardQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option,board_category=None):
        sql=""
        # 게시글 가져오기
        if option == "get":
            sql = f"""

            SELECT 
                   board_no
                 , user_id
                 , board_category
                 , title
                 , content
                 , (SELECT COUNT(1) FROM comment AS A WHERE A.board_no = B.board_no AND A.delete_yn = 'N') AS comment_count
                 , DATE_FORMAT(insert_date, '%Y%m%d%H%i') AS insert_date
                 , DATE_FORMAT(update_date, '%Y%m%d%H%i') AS update_date
              FROM board AS B
             WHERE delete_yn = 'N'
               AND board_category = {board_category}
             ORDER BY B.insert_date DESC

            """

        return sql
    
    
    # 수정 쿼리 만들기
    def make_update_query(self, option,board_no=None,title=None,content=None ):
        sql=""
        # 게시글 수정
        if option == "modify":
            sql = f"""

            UPDATE board
               SET content = '{content}'
                 , title = '{title}'
             WHERE board_no = {board_no}

            """

        # 게시글 삭제
        elif option == "remove":
            sql = f"""

            UPDATE board
               SET delete_yn = 'Y'
             WHERE board_no = {board_no}

            """
        return sql

    # 삽입 쿼리 만들기
    def make_insert_query(self, option,user_id=None,board_category=None,title=None,content=None):
        sql=""
        # 게시글 생성
        if option == "add":
            sql = f"""

            INSERT 
              INTO board(
                   user_id
                 , board_category
                 , title
                 , content)
            VALUES ('{user_id}'
                 , {board_category}
                 , '{title}'
                 , '{content}')

            """

        return sql 







