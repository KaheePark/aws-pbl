# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hell():
#     return "<h1>hello Flask XD <h1>"
#
#
# @app.route('/test')
# def test():
#     # 수행해야 할 로직이 여기 들어온다.
#     return "test"
#
# if __name__ == '__main__':
#     app.run("0.0.0.0",port = 8080)
#

import pymysql
conn = pymysql.connect(host='database-1.cltmc8lqcf9q.ap-northeast-2.rds.amazonaws.com',db='pbldb', port=3306,passwd='Qkrrkgml123!',user='admin')
print(conn)
cursor = conn.cursor()
sql = "select * from practice"
cursor.execute(sql)



conn.commit()
cursor.close()
conn.close()