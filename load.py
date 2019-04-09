import pandas as pd

from   sqlalchemy             import create_engine
from   sqlalchemy.orm         import Session
from   sqlalchemy.ext.automap import automap_base

import pymysql
pymysql.install_as_MySQLdb()

from config import dbuser, dbpasswd, dburi, dbport, dbname

def load_country_tbl(country_df):

    engine = create_engine(f'mysql://{dbuser}:{dbpasswd}@{dburi}:{dbport}/{dbname}')
    Base   = automap_base()

    Base.prepare(engine, reflect='True')

    session   = Session(bind=engine)
    countries = []
    Country   = Base.classes.country

    for cntry_name in country_df['Country']:
        countries.append(Country(name=cntry_name.strip())

    session.add_all(countries)
    session.commit()
    session.close()
        

def load_song_tbl(song_df):

    engine = create_engine(f'mysql://{dbuser}:{dbpasswd}@{dburi}:{dbport}/{dbname}')
    Base   = automap_base()

    Base.prepare(engine, reflect='True')

    session = Session(bind=engine)
    songs   = []
    Song    = Base.classes.song

    for trk_name, artist_name in zip(song_df['Track Name'], song_df['Artists Name']):
        songs.append(Song(title=trk_name.strip(), artist=artist_name.strip())

    session.add_all(songs)
    session.commit()
    session.close()
