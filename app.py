from flask import Flask, request ,jsonify, abort, make_response
from flask_cors import CORS
from utils.board.BoardQueryBuilder import BoardQueryBuilder
from utils.board.CommentQueryBuilder import CommentQueryBuilder
from utils.quiz.BookmarkQueryBuilder import BookmarkQueryBuilder
from utils.quiz.TestHistoryQueryBuilder import TestHistoryQueryBuilder
from utils.quiz.QuizQueryBuilder import QuizQueryBuilder
from utils.quiz.QuizMetaQueryBuilder import QuizMetaQueryBuilder
from utils.subscribe.SubscribeQueryBuilder import SubscribeQueryBuilder
from utils.system.SystemQueryBuilder import SystemQueryBuilder
from utils.user.UserQueryBuilder import UserQueryBuilder
from utils.QueryExecuter import QueryExecuter
import json


application = app = Flask(__name__)
CORS(app)

# 퀴즈 핸들링
@app.route('/quiz/<quiz_category>/<option>/<id>',methods=['GET'])
def get_quiz(quiz_category, option,id):

    try:
        sql = quiz_qb.make_select_query(quiz_category=quiz_category, option=option,id=id)
        app.logger.debug(sql)
        
        result = qe.get_questions(sql=sql)
        app.logger.debug(result)
        return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
         
    except Exception as e:
        print(e)
        abort(500)

# 퀴즈 메타 핸들링
@app.route('/quiz_meta/<option>',methods=['GET','POST'])
def handle_quiz_meta(option):

    try:
        sql = quiz_meta_qb.make_select_query(option)
        app.logger.debug(sql)

        result = qe.get_quiz_metas(sql=sql)
        app.logger.debug(result)
        return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
         
    except Exception as e:
        print(e)
        abort(500)

# 유저 핸들링
@app.route('/user/<option>',methods=['GET','POST'])
def handle_user(option):

    if option == "login":
        try:
            params = request.get_json()
            id = params["id"]
            password = params["password"]

            app.logger.debug(id)
            app.logger.debug(password)

            sql = user_qb.make_select_query(option=option, id=id, password=password)
            app.logger.debug(sql)

            result = qe.get_user(sql=sql)
            app.logger.debug(result)

            if result != (): 
                sql = user_qb.make_insert_query(option="history", user_id=id)
                app.logger.debug(sql)

                qe.add_user_history(sql=sql)

            return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)

    elif option == "password":
        try:
            params = request.get_json()
            id = params["id"]
            password = params["password"]
            new_password = params["new_password"]

            app.logger.debug(id)
            app.logger.debug(password)
            app.logger.debug(new_password)

            sql = user_qb.make_update_query(option=option, id=id, password=password,new_password=new_password)
            app.logger.debug(sql)

            result = qe.modify_user_password(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "history":
        try:
            params = request.get_json()
            id = params["id"]

            app.logger.debug(id)

            sql = user_qb.make_insert_query(option="history", user_id=id)
            app.logger.debug(sql)

            result =  qe.add_user_history(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)



# 시험이력 핸들링
@app.route('/test/history/<option>/<user_id>',methods=['GET','POST'])
def handle_test_history(option,user_id):

    if option == "add":
        try:
            params = request.get_json()
            user_id = params["user_id"]
            quiz_no = params["quiz_no"]
            question_no_group = params["question_no_group"]
            correct_group = params["correct_group"]
            checked_group = params["checked_group"]
            question_score_group = params["question_score_group"]
            user_answer_group = params["user_answer_group"]
            test_score = params["test_score"]
            submission_yn = params["submission_yn"]

            app.logger.debug(user_id)
            app.logger.debug(quiz_no)
            app.logger.debug(question_no_group)
            app.logger.debug(correct_group)
            app.logger.debug(checked_group)
            app.logger.debug(question_score_group)
            app.logger.debug(user_answer_group)
            app.logger.debug(test_score)
            app.logger.debug(submission_yn)

            sql = test_history_qb.make_insert_query(
                option=option, 
                user_id=user_id, 
                quiz_no=quiz_no,
                question_no_group=question_no_group,
                correct_group=correct_group,
                checked_group=checked_group,
                question_score_group=question_score_group,
                user_answer_group=user_answer_group,
                test_score=test_score,
                submission_yn=submission_yn,
            )

            app.logger.debug(sql)

            result = qe.add_test_hisotory(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "get":
        try:

            app.logger.debug(user_id)

            sql = test_history_qb.make_select_query(
                option=option, 
                user_id=user_id,
            )

            app.logger.debug(sql)

            result = qe.get_test_history(sql=sql)
            app.logger.debug(result)

            return  json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)
    elif option == "remove":
        try:
            params = request.get_json()
            user_id = params["user_id"]
            quiz_no = params["quiz_no"]
            test_history_no = params["test_history_no"]
           

            app.logger.debug(user_id)
            app.logger.debug(quiz_no)
            app.logger.debug(test_history_no)


            sql = test_history_qb.make_update_query(
                        option, 
                        test_history_no, 
                        user_id, 
                        quiz_no
                    )


            app.logger.debug(sql)

            result = qe.remove_test_hisotory(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)
        

# 북마크 핸들링
@app.route('/bookmarks/<option>',methods=['GET','POST'])
def handle_bookmarks(option):

    if option == "add":
        try:
            params = request.get_json()
            user_id = params["user_id"]
            quiz_no = params["quiz_no"]
            question_no = params["question_no"]

            app.logger.debug(user_id)
            app.logger.debug(quiz_no)
            app.logger.debug(question_no)

            sql = bookmark_qb.make_select_query(
                        option="exist", 
                        user_id=user_id, 
                        quiz_no=quiz_no,
                        question_no =question_no
                    )

            app.logger.debug(sql)

            result = qe.get_bookmark(sql=sql)
            app.logger.debug(result)
            app.logger.debug(result[0]['exist'])

            if (result[0]['exist'] >= 1) :

                sql = bookmark_qb.make_update_query(
                            option=option, 
                            user_id=user_id, 
                            quiz_no=quiz_no,
                            question_no =question_no
                        )
            
            else:
                sql = bookmark_qb.make_insert_query(                    
                            option=option, 
                            user_id=user_id, 
                            quiz_no=quiz_no,
                            question_no =question_no
                        )

            app.logger.debug(sql)

            result = qe.add_bookmark(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "remove":
        try:
            params = request.get_json()
            user_id = params["user_id"]
            quiz_no = params["quiz_no"]
            question_no = params["question_no"]

            app.logger.debug(user_id)
            app.logger.debug(quiz_no)
            app.logger.debug(question_no)

            sql = bookmark_qb.make_update_query(
                        option=option, 
                        user_id=user_id, 
                        quiz_no=quiz_no,
                        question_no =question_no
                    )

            app.logger.debug(sql)

            result = qe.remove_bookmark(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "get":
        try:
            params = request.get_json()
            user_id = params["user_id"]

            app.logger.debug(user_id)

            sql = bookmark_qb.make_select_query(
                        option=option, 
                        user_id=user_id, 
                    )

            app.logger.debug(sql)

            bookmarks = qe.get_bookmarks(sql=sql)
            app.logger.debug(bookmarks)

            return  json.dumps(bookmarks, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)
    
# 구독 핸들링
@app.route('/subscribe/<option>',methods=['GET','POST'])
def handle_subscribe(option):

    if option == "products":
        try:
            sql = subscribe_qb.make_select_query(option=option,)
            app.logger.debug(sql)

            result = qe.get_subscribe_products(sql=sql)
            app.logger.debug(result)

            return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)

    elif option == "state":
        try:
            params = request.get_json()

            user_id = params["user_id"]
            app.logger.debug(user_id)

            sql = subscribe_qb.make_select_query(option=option, user_id=user_id)
            app.logger.debug(sql)

            result = qe.get_subscribe(sql=sql)
            app.logger.debug(result)

            return  json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

# 게시글 핸들링
@app.route('/board/<option>',methods=['POST'])
def handle_board_post(option):
    if option == "add":
        try:
            params = request.get_json()

            user_id = params["user_id"]
            board_category = params["board_category"]
            content = params["content"]
            title = params["title"]
            app.logger.debug(user_id)
            app.logger.debug(board_category)
            app.logger.debug(content)
            app.logger.debug(title)

            sql = board_qb.make_insert_query(option=option, user_id=user_id,board_category=board_category, content=content, title=title)
            app.logger.debug(sql)

            result = qe.add_board(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "modify":
        try:
            params = request.get_json()

            board_no = params["board_no"]
            content = params["content"]
            title = params["title"]
            app.logger.debug(board_no)
            app.logger.debug(content)
            app.logger.debug(title)

            sql = board_qb.make_update_query(option=option, board_no=board_no, content=content, title=title)
            app.logger.debug(sql)

            result = qe.modify_board(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)
    
    elif option == "remove":
        try:
            params = request.get_json()

            board_no = params["board_no"]
            app.logger.debug(board_no)

            sql = board_qb.make_update_query(option=option, board_no=board_no)
            app.logger.debug(sql)

            result = qe.remove_board(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

# 게시글 핸들링
@app.route('/board/get/<board_category>',methods=['GET'])
def handle_board_get(board_category):
    try:
        sql = board_qb.make_select_query(option='get',board_category=board_category)
        app.logger.debug(sql)

        result = qe.get_boardlist(sql=sql)
        app.logger.debug(result)

        return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
    except Exception as e:
        print(e)
        abort(500)


# 댓글 핸들링
@app.route('/comment/<option>',methods=['POST'])
def handle_comment_post(option):

    if option == "add":
        try:
            params = request.get_json()

            board_no = params["board_no"]
            user_id = params["user_id"]
            content = params["content"]
            app.logger.debug(board_no)
            app.logger.debug(user_id)
            app.logger.debug(content)

            sql = comment_qb.make_insert_query(option=option, user_id=user_id, board_no=board_no, content=content)
            app.logger.debug(sql)

            result = qe.add_comment(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "modify":
        try:
            params = request.get_json()

            comment_no = params["comment_no"]
            content = params["content"]

            app.logger.debug(comment_no)
            app.logger.debug(content)

            sql = comment_qb.make_update_query(option=option, content=content, comment_no=comment_no)
            app.logger.debug(sql)

            result = qe.modify_comment(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)
    
    elif option == "remove":
        try:
            params = request.get_json()

            comment_no = params["comment_no"]
            app.logger.debug(comment_no)

            sql = comment_qb.make_update_query(option=option, comment_no=comment_no)
            app.logger.debug(sql)

            result = qe.remove_comment(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

    elif option == "remove_all":
        try:
            params = request.get_json()

            board_no = params["board_no"]
            app.logger.debug(board_no)

            sql = comment_qb.make_update_query(option=option, board_no=board_no)
            app.logger.debug(sql)

            result = qe.remove_all_comment(sql=sql)
            app.logger.debug(result)

            return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
        except Exception as e:
            print(e)
            abort(500)

# 댓글 핸들링
@app.route('/comment/get/<board_no>',methods=['GET'])
def handle_comment_get(board_no):

    try:
        sql = comment_qb.make_select_query(option='get', board_no=board_no)
        app.logger.debug(sql)

        result = qe.get_comments(sql=sql)
        app.logger.debug(result)

        return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
    except Exception as e:
        print(e)
        abort(500)

# 시스템로그 핸들링
@app.route('/system/log/<option>',methods=['GET'])
def handle_system_log_get(option):
    if option=="login":
        try:
            sql = system_qb.make_select_query(option=option)
            app.logger.debug(sql)

            result = qe.get_logins(sql=sql)
            app.logger.debug(result)

            return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)

    elif option=="login_cnt":
        try:
            sql = system_qb.make_select_query(option=option)
            app.logger.debug(sql)

            result = qe.get_logins_cnt(sql=sql)
            app.logger.debug(result)

            return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)

    elif option=="test":
        try:
            sql = system_qb.make_select_query(option=option)
            app.logger.debug(sql)

            result = qe.get_tests(sql=sql)
            app.logger.debug(result)

            return json.dumps(result, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
            
        except Exception as e:
            print(e)
            abort(500)

# 커밋테스트
# @app.route('/test/',methods=['get'])
# def commit_test():
#     try:


#         sql = user_qb.make_insert_query(option="history", id="hus2112")
#         app.logger.debug(sql)

#         result =  qe.add_user_history(sql=sql)
#         app.logger.debug(result)

#         return  json.dumps({"success_cnt":result}, ensure_ascii=False) #ensure_ascii=False 없으면 한글 깨짐
        
#     except Exception as e:
#         print(e)
#         abort(500)

if __name__ =='__main__':
    # qb = QueryBuilder
    # qe = QueryExcuter

    quiz_qb = QuizQueryBuilder()
    quiz_meta_qb = QuizMetaQueryBuilder()
    user_qb = UserQueryBuilder()
    test_history_qb = TestHistoryQueryBuilder()
    bookmark_qb = BookmarkQueryBuilder()
    subscribe_qb = SubscribeQueryBuilder()
    board_qb = BoardQueryBuilder()
    comment_qb = CommentQueryBuilder()
    system_qb = SystemQueryBuilder()
    qe = QueryExecuter()
    app.run(host="0.0.0.0",port=5000, debug=False,)