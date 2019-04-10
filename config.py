## CONFIG for chromedriver
from splinter import Browser

#### Mac Users ####
# chromedriver_path = !which chromedriver

# executable_path = {'executable_path': chromedriver_path[0]}

#### Windows Users ####
executable_path = {'executable_path': 'Resources/chromedriver.exe'}



## CONFIG for Database Connection
database = 'top50_db'

username = 'root'

password = 'root'

host = '127.0.0.1'

port = 3306

connection_string = f"{username}:{password}@{host}:{port}/{database}"