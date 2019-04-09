import extract
from extract import excelVBA_to_df, csv_to_df
from transform import playlist, song, country


#### Transform Playlist DataFrame ####
path = "Resources/Top50_Playlist_by_Country.xlsm"

playlist_df = excelVBA_to_df(path)

playlist_transformed = playlist(playlist_df)



#### Transform Song DataFrame ####
from pathlib import Path

# Root directory to CSV Folder
rootdir = Path('Country CSV Files')

# Loops through each csv file in Top Country CSV folder
file_list = [f for f in rootdir.glob("*.csv") if f.is_file()]

# Convert first csv into DataFrame
song_df = csv_to_df(file_list[0])

# Loop starts at second file and ends at last
for file in file_list[1:]:
    
    # Convert excel into DataFrame
    df = csv_to_df(file)
    
    # Add each country DataFrame onto the first
    song_df = song_df.append(df)

song_transformed = song(song_df)


#### Transform Country DataFrame ####
path = "Resources/countryISO.csv"

country_df = csv_to_df(path)

country_transformed = country(country_df)


#### LOAD Dataframes to SQL Database####
print("-----------------------------------------------\nLoading DataFrames into SQL Database\n-----------------------------------------------")

from load import create_engine, connection_string, engine, df_to_sql

df_to_sql(playlist_transformed, "playlist")
df_to_sql(song_transformed, "song")
df_to_sql(country_transformed, "country")

print("-----------------------------------------------\nFinished Loading into SQL Database\n-----------------------------------------------")