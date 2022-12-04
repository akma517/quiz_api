class QuizQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, quiz_category, option, id):
        sql=""
        # 랜덤으로 문제 가져오기
        if option == "test":
            sql = f"""

            SELECT 
                   quiz_no
                 , question_no
                 , question
                 , question_kor
                 , answer
                 , a
                 , b
                 , c
                 , d
                 , e
                 , f
                 , g
                 , a_kor
                 , b_kor
                 , c_kor
                 , d_kor
                 , e_kor
                 , f_kor
                 , g_kor        
                 , (CASE WHEN EXISTS(SELECT 
                                            question_no 
                                       FROM bookmarks AS B
                                      WHERE B.question_no = A.question_no 
                                        AND B.user_id = '{id}'
                                        AND B.quiz_no = A.quiz_no
                                        AND B.delete_yn = 'N') 
                         THEN 'Y' 
                         ELSE 'N' 
                         END) AS bookmarked
              FROM quiz AS A
             WHERE quiz_no ={quiz_category} 
             ORDER BY rand() limit 75

            """

        # 시험이력 확인위해 퀴즈 전체가져오기
        elif option =="order_all" and quiz_category == '0':
            sql = f"""

            SELECT
                   quiz_no
                 , question_no
                 , question
                 , question_kor
                 , answer
                 , a
                 , b
                 , c
                 , d
                 , e
                 , f
                 , g
                 , a_kor
                 , b_kor
                 , c_kor
                 , d_kor
                 , e_kor
                 , f_kor
                 , g_kor
                 , (CASE WHEN EXISTS(SELECT 
                                            question_no 
                                       FROM bookmarks AS B
                                      WHERE B.question_no = A.question_no 
                                        AND B.user_id = '{id}'
                                        AND B.quiz_no = A.quiz_no
                                        AND B.delete_yn = 'N') 
                         THEN 'Y' 
                         ELSE 'N' 
                         END) AS bookmarked
              FROM quiz AS A
             ORDER BY quiz_no
                 , question_no


            """
        
        # 순서대로 문제 가져오기
        elif option =="order_all":
            sql = f"""

	        SELECT
                   quiz_no
                 , question_no
                 , question
                 , question_kor
                 , answer
                 , a
                 , b
                 , c
                 , d
                 , e
                 , f
                 , g
                 , a_kor
                 , b_kor
                 , c_kor
                 , d_kor
                 , e_kor
                 , f_kor
                 , g_kor
                 , (CASE WHEN EXISTS(SELECT 
                                            question_no 
                                       FROM bookmarks AS B
                                      WHERE B.question_no = A.question_no 
                                        AND B.user_id = '{id}'
                                        AND B.quiz_no = A.quiz_no
                                        AND B.delete_yn = 'N') 
                         THEN 'Y' 
                         ELSE 'N' 
                         END) AS bookmarked
              FROM quiz AS A
             WHERE quiz_no = {quiz_category}
          ORDER BY question_no;

            """

        return sql





