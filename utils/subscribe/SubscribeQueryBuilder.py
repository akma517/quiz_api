class SubscribeQueryBuilder:
    """
    쿼리 생성자
    """
    
    # 조회 쿼리 만들기
    def make_select_query(self, option, user_id=None ):
        sql=""
        # 구독상품 가져오기
        if option == "products":
            sql = f"""

            SELECT 
                   subscribe_no
                 , subscribe_name
                 , subscribe_period_name
                 , price
                 , period
                 , description
              FROM subscribe_product
             WHERE delete_yn = 'N'			   

            """
        elif option == "state":
            sql = f"""

            SELECT 
                   B.subscribe_no
                 , A.subscribe_name
                 , A.subscribe_period_name
                 , A.price
                 , A.period
                 , A.description
                 , DATE_FORMAT(B.start_date,'%Y%m%d') AS start_date
                 , DATE_FORMAT(B.end_date,'%Y%m%d') AS end_date
                 , IFNULL(DATE_FORMAT(DATE_ADD(B.end_date,INTERVAL 1 DAY),'%Y%m%d'), '99991231') AS payment_date
                 , B.continue_yn
              FROM subscribe_product AS A
                 , subscribe_history AS B
             WHERE B.delete_yn = 'N'
               AND A.subscribe_no = B.subscribe_no
               AND B.user_id = '{user_id}'
               AND DATE_FORMAT(NOW(),'%Y%m%d') >= start_date
               AND DATE_FORMAT(NOW(),'%Y%m%d') <= end_date

            """
        return sql
    








