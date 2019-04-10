# Spotify ETL

This pipeline extracts data from [Top50_Playlist_by_Country](Resources/Top50_Playlist_by_Country.xlsm), containing playlist ID for API data extraction. It also scrapes [URL](https://www.nationsonline.org/oneworld/country_code_list.htm) for country code. The goal is to move data from the wild web into a structured MySQL database.

### Repo contents

- [`schema_db.sql`](schema_db.sql) contains MySQL database schema (`CREATE DATABASE`, `USE DATABASE`, and `CREATE TABLE` statements)
- [`config.py`](config.py) contains client credentials to access API endpoints and database credentials for local MySQL instances
- [`extract.py`](extract.py) contains scripts used to extract data from API endpoints and scrape data from web source
- [`transform.py`](transform.py) contains functions used to simplify and/or clean the data.
- [`load.py`](load.py) contains functions used to load transformed data into the SQL database
- [`app.py`](app.py) main file for data extraction and loading into database

## Before Starting

Setting up Spotify sign in for API is found here:
[Spotify developer sign up](https://developer.spotify.com/dashboard/applications/4b454f446d1f479082eec9de1c27a4a8 "Spotify API")



For your config.py, to obtain your own client\_id and client\_secret go to the link above and login. 
 
 - Once logged in click *CREATE A CLIENT ID*

Once you setup your app you should be able to click on your app to obtain your very own client_id and client_secret.

Some module you will need to run [`app.py`](app.py) are PyMySQL / bs4 / SQLAlchemy  
Installation can ber accomplished with:

- pip install PyMySQL
- pip install bs4
- pip install SQLAlchemy

 
## ETL Procedure

### Step 1:

 - Run [`schema_db.sql`](schema_db.sql) first to create database and tables

 **Note:**  
 This schema includes a `DROP DATABASE IF EXISTS top50_db` and will remove existing database with the `top50_db` name.


**Example**  

```
(PyEnv) user $ mysql -u<user name> -p<your password> -h127.0.0.1

Welcome to the MySQL monitor.

mysql> source schema_db.sql
Query OK, 0 rows affected, 1 warning (0.00 sec)

Query OK, 1 row affected (0.00 sec)

Database changed
Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.01 sec)

Query OK, 0 rows affected (0.01 sec)

mysql> 
```  

This will build SQL DB in MySQL from the command line. The schema can also be run from a GUI of your choice.

### Step 2:
 - **Rename** [`config_temp.py`](config_temp.py) to [`config.py`](config.py). 
 - Update the database credentials for your local MySQL instance. **Be aware** that SQLAlchemy uses different Dialects and the string for connecting to MySQL can be 'mysql' or 'mysql+pymysql' depending on your environment. This will be set in `config.py` as `dialect =`.
 - Update your client credentials for Spotify API.

### Step 3:

From project folder, run:

```
$ python app.py
```

 


 - Run `python app.py` to extract data and load into SQL database
 
