
DROP DATABASE IF EXISTS global_top50_db;

CREATE DATABASE global_top50_db;

USE global_top50_db;


-- create the database tables --


CREATE TABLE country (

    country_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    name       VARCHAR(50) NOT NULL,

    PRIMARY KEY (country_id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE song (

    song_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    title   VARCHAR(70) NOT NULL,
    artist  VARCHAR(70),

    PRIMARY KEY (song_id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE playlist (
    
    playlist_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    title       VARCHAR(30) NOT NULL,
    country_id  INT UNSIGNED NOT NULL,

    PRIMARY KEY (playlist_id),

    KEY idx_fk_country_id (country_id),
    CONSTRAINT fk_playlist_country FOREIGN KEY (country_id) REFERENCES country(country_id) ON DELETE RESTRICT ON UPDATE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE playlist_item (
    
    id          INT UNSIGNED AUTO_INCREMENT NOT NULL,
    playlist_id INT UNSIGNED NOT NULL,
    song_id     INT UNSIGNED NOT NULL,

    PRIMARY KEY (id),

    KEY idx_fk_playlist_id (playlist_id),
    KEY idx_fk_song_id (song_id),
    CONSTRAINT fk_playlist_item_playlist FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_playlist_item_song FOREIGN KEY (song_id) REFERENCES song(song_id) ON DELETE RESTRICT ON UPDATE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
