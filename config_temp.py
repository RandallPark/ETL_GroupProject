## CONFIG for API Connection
client_id = "4b454f446d1f479082eec9de1c27a4a8"
client_secret = "e639450422594948b17c46d1a82f4882"


## CONFIG for Database Connection
dialect = 'mysql+pymysql'
database = 'top50_db'
username = 'root'
password = 'root'
host = '127.0.0.1'
port = 3306

connection_string = f"{dialect}://{username}:{password}@{host}:{port}/{database}"