import extract
from extract import excelVBA_to_df, csv_to_df, top50_playlist_df, song_df, countryISO_df
from transform import playlist, song, artist, country

#### Transform Playlist DataFrame ####
playlist_transformed = playlist(top50_playlist_df)


#### Transform Song DataFrame ####
song_transformed = song(song_df)


#### Transform Artist DataFrame ####
artist_transformed = artist(song_df)


#### Transform Country DataFrame ####
country_transformed = country(countryISO_df)


#### LOAD Dataframes to SQL Database####
print("-------------------------------------------\nLoading DataFrames into SQL Database\n-------------------------------------------")

from config import connection_string
from load import df_to_sql
import load

df_to_sql(playlist_transformed, "playlist")
df_to_sql(song_transformed, "song")
df_to_sql(artist_transformed, "artist")
df_to_sql(country_transformed, "country")

print("-------------------------------------------\nFinished Loading into SQL Database\n-------------------------------------------")