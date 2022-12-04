class SystemQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option):
        sql=""
        # 로그인하기
        if option == "login":
            sql = f"""

            SELECT 
                   user_id
                 , DATE_FORMAT(login_date, '%Y%m%d%H%i%s') AS login_date
              FROM login_history AS A
             WHERE delete_yn = 'N'
               AND user_id <> 'hus2112' 
             ORDER BY A.login_date DESC 
			       LIMIT 1000

            """
        elif option == "login_cnt":
            sql = f"""

            SELECT 
                   user_id
                 , COUNT(1) AS cnt
              FROM login_history AS A
             WHERE delete_yn = 'N'
               AND user_id <> 'hus2112' 
             GROUP BY user_id

            """
        elif option == "test":
            sql = f"""

            SELECT 
                   user_id
                 , DATE_FORMAT(test_date, '%Y%m%d%H%i%s') AS test_date
              FROM test_history AS A
             WHERE delete_yn = 'N'
               AND user_id <> 'hus2112' 
             ORDER BY A.test_date DESC 
			       LIMIT 1000

            """
        return sql
    
    