## 모듈 로딩
import os

## 다양한 DBMS URI - SQLITE
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

## 다양한 DBMS URI
DB_SQLITE_URI = f"sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}"      # 내컴
DB_MYSQL_URI = 'mysql+pymysql://root:0000@localhost:3306/testdb'           # 원격
                                # id : pw
                                
# DB_MARAI_URI = 'mariadb+mariadb://root:root@localhost:0000/testdb'
# DB_POST_URi = "postgresql+pg8000://scott:tiger@localhost/test"

# 사용할 DBMS 설정 / SQLALCHEMY_시작 변수명 고정 
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 위 둘은 환경 변수라서 변수명을 반드시 저걸로 해주어야 함




# MYSQL_CONFIG = {
#     'host': '1.251.203.204:33065',
#     'user': 'root',
#     'password': 'kdt5',
#     'database': 'Team5'
# }

# DB_MYSQL_URL = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
#     **MYSQL_CONFIG
# )

# SQLALCHEMY_DATABASE_URI = DB_MYSQL_URL
# SQLALCHEMY_TRACK_MODIFICATIONS = False