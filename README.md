# Spotify ETL

This pipeline extracts data from [Top50_Playlist_by_Country](Resources/Top50_Playlist_by_Country.xlsm), containing playlist ID for API data extraction. It also scrapes [URL](https://www.nationsonline.org/oneworld/country_code_list.htm) for country code. The goal is to move data from the wild web into a structured MySQL database.

## Files

- [`schema_db.sql`](schema_db.sql) contains MySQL database schema (`CREATE DATABASE`, `USE DATABASE`, and `CREATE TABLE` statements)
- [`config.py`](config.py) contains client credentials to access API endpoints and database credentials for local MySQL instances
- [`extractor.py`](extractor.py) contains scripts used to extract data from API endpoints and scrape data from web source
- [`transformer.py`](transformer.py) contains functions used to simplify and/or clean the data.
- [`loader.py`](loader.py) contains functions used to load transformed data into the SQL database
- [`app.py`](app.py) main file for data extraction and loading into database
 
## To Run
 
 - Run [`schema_db.sql`](schema_db.sql) first to create database and tables
 - Update the database credentials for your local MySQL instance or update your client credentials through [`config.py`](config.py)
 - Run `python app.py` to extract data and load into SQL database
 
## TODO

To obtain your own client_id and client_secret go to (https://developer.spotify.com/dashboard/applications/4b454f446d1f479082eec9de1c27a4a8) and login. Then click on "CREATE A CLIENT ID", once you setup your app you should be able to click on your app to obtain your very own client_id and client_secret.

Install any necessary modules to run [app](app.py)

Modules you may need: PyMySQL, bs4, SQLAlchemy
  -pip install PyMySQL
  -pip install bs4
  -pip install SQLAlchemy
