import pandas as pd

from   sqlalchemy             import create_engine
from   sqlalchemy.orm         import Session
from   sqlalchemy.ext.automap import automap_base

import pymysql
pymysql.install_as_MySQLdb()

from config import dbuser, dbpasswd, dburi, dbport, dbname

def load_country_tbl(country_df):

    try:
        engine = create_engine(f'mysql://{dbuser}:{dbpasswd}@{dburi}:{dbport}/{dbname}')
        Base   = automap_base()

        Base.prepare(engine, reflect='True')

        session   = Session(bind=engine)
        countries = []
        Country   = Base.classes.country

        for cntry_name, cntry_code in zip(country_df['Country'], list(country_df.index)):
            countries.append(Country(name=cntry_name.strip(), country_code=cntry_code.strip()))

        session.add_all(countries)
        session.commit()
        session.close()
    except:
        print('ERROR: An error occurred during processing in load_country_tbl()')
        return False
    else:
        return True
        

def load_song_tbl(song_df):

    try:
        engine = create_engine(f'mysql://{dbuser}:{dbpasswd}@{dburi}:{dbport}/{dbname}')
        Base   = automap_base()

        Base.prepare(engine, reflect='True')

        session = Session(bind=engine)
        songs   = []
        Song    = Base.classes.song

        for song_name, song_id in zip(song_df['song_name'], song_df['song_id']):
            songs.append(Song(title=song_name.strip(), spotify_id=song_id.strip()))

        session.add_all(songs)
        session.commit()
        session.close()
    except:
        print('ERROR: An error occurred during processing in load_song_tbl()')
        return False
    else:
        return True
