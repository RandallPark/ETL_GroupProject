import numpy as np
## Transform Playlist DataFrame

def playlist(df):
    # Create a filtered dataframe from specific columns
    playlist_col = ["Country", "Spotify URL", "Spotify Playlist ID"]

    playlist_transformed = df[playlist_col].copy()

    # Rename the column headers
    playlist_transformed = playlist_transformed.rename(columns={"Country": "country_code",
                                                            "Spotify URL": "spotify_url",
                                                            "Spotify Playlist ID": "playlist_id"})

    playlist_transformed.index.names = ["id"]

    return playlist_transformed


## Transform Song DataFrame

def song(df):
    # Create a filtered dataframe from specific columns
    song_col = ["ID", "Track Name", "Track ID", "Artist ID"]

    song_transformed = df[song_col].copy()

    # Rename the column headers
    song_transformed = song_transformed.rename(columns={"ID": "id",
                                                        "Track Name": "song_name",
                                                        "Track ID": "song_id",
                                                        "Artist ID": "artist_id"})

    song_transformed = song_transformed.set_index("id")

    return song_transformed


## Transform Country DataFrame

def country(df):
    # Create a filtered dataframe from specific columns
    country_col = ["Country", "Alpha_2", "Alpha_3_Code", "UN_Code"]
    # Create a filtered dataframe from specific columns
    country_transformed = df[country_col].copy()

    # Replace empty cells with NaN
    country_transformed.replace('', np.nan, inplace=True)

    # Drop rows with empty cells
    country_transformed = country_transformed.dropna()

    # Rename the column headers
    country_transformed = country_transformed.rename(columns={"Country": "country_name",
                                                            "Alpha_2": "alpha_2",
                                                            "Alpha_3_Code": "country_code",
                                                            "UN_Code": "un_code"})

    country_transformed = country_transformed.set_index("country_code")

    return country_transformed