HOST = "127.0.0.1"
PORT = "3306"
DB = ""
USER = "root"
PASS = ""
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASS, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI