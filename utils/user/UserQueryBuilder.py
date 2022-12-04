class UserQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option, id, password=None,auth=None):
        sql=""
        # 로그인하기
        if option == "login":
            sql = f"""

            SELECT 
                   id
                 , name
                 , (CASE WHEN auth = 99 then auth
                         WHEN (SELECT B.subscribe_name
                                 FROM subscribe_history AS A
                                    , subscribe_product AS B 
                                WHERE A.user_id = '{id}' 
                                  AND A.subscribe_no = B.subscribe_no
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) ='plain' THEN 2 
                         WHEN (SELECT B.subscribe_name 
                                 FROM subscribe_history AS A
                                    , subscribe_product AS B 
                                WHERE A.user_id = '{id}' 
                                  AND A.subscribe_no = B.subscribe_no
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) ='super' THEN 3
                         WHEN (SELECT B.subscribe_name 
                                 FROM subscribe_history AS A
                                    , subscribe_product AS B 
                                WHERE A.user_id = '{id}' 
                                  AND A.subscribe_no = B.subscribe_no
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                                  AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) ='kico' THEN 4	   
                        ELSE auth END) AS auth
                 , (SELECT IFNULL(B.subscribe_name, 'None' )
                      FROM subscribe_history AS A
                         , subscribe_product AS B 
                     WHERE A.user_id = '{id}' 
                       AND A.subscribe_no = B.subscribe_no
                       AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                       AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) AS subscribe_name
                 , (SELECT IFNULL(DATE_FORMAT(start_date, '%Y%m%d'),'None')
                      FROM subscribe_history
                     WHERE user_id = '{id}'
                       AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                       AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) AS start_date
                 , (SELECT IFNULL(DATE_FORMAT(end_date, '%Y%m%d'),'None')
                      FROM subscribe_history
                     WHERE user_id = '{id}'
                       AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
                       AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date) AS end_date
              FROM user 
             WHERE id = '{id}'
               AND password = PASSWORD('{password}');

            """

        return sql
    
    
    # 수정 쿼리 만들기
    def make_update_query(self, option, id, password=None, new_password=None,auth=None ):
        sql=""
        # 비밀번호변경하기
        if option == "password":
            sql = f"""

            UPDATE user
               SET password = PASSWORD('{new_password}')
             WHERE id = '{id}'
               AND password = PASSWORD('{password}')

            """
        
        return sql

    # 삽입 쿼리 만들기
    def make_insert_query(self, user_id, option):
        sql=""
        # 로그인 이력 넣기
        if option == "history":
            sql = f"""

            INSERT 
              INTO login_history(user_id)
            VALUES ('{user_id}')

            """
        
        return sql    








