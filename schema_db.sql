DROP DATABASE IF EXISTS top50_db;

CREATE DATABASE top50_db;

USE top50_db;


-- create the database tables --


CREATE TABLE country (
	country_code varchar(3) NOT NULL,
    country_name varchar(50) NOT NULL,
	alpha_2 varchar(50) NOT NULL,
    un_code INT NOT NULL,

	PRIMARY KEY (country_code)
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE song (
	id INT NOT NULL,
    song_name varchar(100) NOT NULL,
    song_id varchar(100) NOT NULL,
    artist_id varchar(100) NOT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE artist (
    artist_id varchar(100) NOT NULL,
    artist_name varchar(100) NOT NULL,
    
    PRIMARY KEY (artist_id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE playlist (
	id INT NOT NULL,
    country_code varchar(3) NOT NULL,
    spotify_url varchar(100) NOT NULL,
    playlist_id varchar(100) NOT NULL,
    
    PRIMARY KEY (id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;