from pathlib import Path
import pandas as pd
import numpy as np

# Root directory to Top Country CSV folder
rootdir = Path('Top Country CSV')

# Loops through each csv file in Top Country CSV folder
file_list = [f for f in rootdir.glob("*.csv") if f.is_file()]

# Store country name
country_name = str(file_list[0]).split("\\")[-1].split("_")[0]

# Convert first csv into DataFrame
song_df = pd.read_csv(file_list[0])

# Drops unecessary column
song_df = song_df.drop(columns = 'Unnamed: 0')

# Insert country name column
song_df.insert(0, "Country", country_name)

# Loop starts at second file and ends at last
for file in file_list[1:]:
    song_name = str(file).split("\\")[-1].split("_")[0]
    
    # Convert excel into DataFrame
    df = pd.read_csv(file)
    
    # Drop unecessary columns and insert country
    df = df.drop(columns = 'Unnamed: 0')
    df.insert(0, "Country", country_name)
    
    # Add each country DataFrame onto the first
    song_df = song_df.append(df)

song_df = song_df[["Country", "Track Name", "Track ID", "Artists Name"]]