class TestHistoryQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option, user_id):
        sql=""
        # 시험이력 가져오기
        if option == "get":
            sql = f"""

            SELECT
                  test_history_no
                , user_id
                , quiz_no
                , question_no_group
                , correct_group
                , checked_group
                , question_score_group
                , user_answer_group
                , test_score
                , submission_yn
                , DATE_FORMAT(test_date, '%Y%m%d%H%i') AS test_date
                , (SELECT image_path FROM quiz_meta WHERE quiz_no = quiz_no) AS image_path
                , (SELECT quiz_name FROM quiz_meta WHERE quiz_no = quiz_no) AS quiz_name
                , (SELECT pass_score FROM quiz_meta WHERE quiz_no = quiz_no) AS pass_score
             FROM test_history AS A
            WHERE user_id = '{user_id}'
              AND delete_yn = 'N'
            ORDER BY A.test_date desc 

            """

        return sql
    
    
    # 수정 쿼리 만들기
    def make_update_query(self, option, test_history_no, user_id, quiz_no):
        sql=""

        # 논리적 삭제
        if option == "remove":
            sql = f"""

            UPDATE test_history
               SET delete_yn = 'Y'
             WHERE test_history_no = {test_history_no}
               AND user_id = '{user_id}'
               AND quiz_no = {quiz_no}

            """

        return sql

    # 삽입 쿼리 만들기
    def make_insert_query(
                self,
                option,
                user_id, 
                quiz_no,
                question_no_group,
                correct_group,
                checked_group,
                question_score_group,
                user_answer_group,
                test_score,
                submission_yn,
                ):
        sql=""
        # 시험이력 삽입
        if option == "add":
            sql = f"""

            INSERT 
              INTO test_history(
                   user_id
                 , quiz_no
                 , question_no_group
                 , correct_group
                 , checked_group
                 , question_score_group
                 , user_answer_group
                 , test_score
                 , submission_yn)
            VALUES ('{user_id}'
                 , {quiz_no}
                 , '{question_no_group}'
                 , '{correct_group}'
                 , '{checked_group}'
                 , '{question_score_group}'
                 , '{user_answer_group}'
                 , {test_score}
                 , '{submission_yn}')

            """

        return sql







