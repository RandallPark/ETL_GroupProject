import extract
from extract import excelVBA_to_df, csv_to_df, top50_playlist_df, song_df, countryISO_df
from transform import playlist, song, country

#### Transform Playlist DataFrame ####
playlist_transformed = playlist(top50_playlist_df)


#### Transform Song DataFrame ####
song_transformed = song(song_df)


#### Transform Country DataFrame ####
country_transformed = country(countryISO_df)


#### LOAD Dataframes to SQL Database####
print("-------------------------------------------\nLoading DataFrames into SQL Database\n-------------------------------------------")

from load import create_engine, connection_string, engine, df_to_sql

df_to_sql(playlist_transformed, "playlist")
df_to_sql(song_transformed, "song")
df_to_sql(country_transformed, "country")

print("-------------------------------------------\nFinished Loading into SQL Database\n-------------------------------------------")