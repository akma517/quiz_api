class QuizMetaQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option):
        sql=""
        # app 시작시 퀴즈 리스트들 메타정보 가져오기
        if option == "app_init":
            sql = f"""

            SELECT 
                   quiz_no
                 , quiz_name
                 , test_time
                 , test_question_count
                 , total_score 
                 , pass_score
                 , image_path
                 , zero_score_yn
                 , (SELECT GROUP_CONCAT(question_score)
					                    FROM test_meta B
											WHERE B.quiz_no = A.quiz_no) AS question_scores
					       , (SELECT GROUP_CONCAT(question_score_count)
					                    FROM test_meta B
											WHERE B.quiz_no = A.quiz_no) AS question_score_counts
              FROM quiz_meta A
             WHERE delete_yn = 'N'
             ORDER BY quiz_no

            """

        return sql







