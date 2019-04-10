
DROP DATABASE IF EXISTS global_top50_db;

CREATE DATABASE global_top50_db;

USE global_top50_db;


-- create the database tables --


CREATE TABLE country (

    id           INT UNSIGNED AUTO_INCREMENT NOT NULL,
    name         VARCHAR(50) NOT NULL,
    country_code VARCHAR(3) NOT NULL,

    PRIMARY KEY (id),
    UNIQUE  KEY (country_code)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE song (

    id          INT UNSIGNED AUTO_INCREMENT NOT NULL,
    title       VARCHAR(70) NOT NULL,
    spotify_id  VARCHAR(30) NOT NULL,

    PRIMARY KEY (id),
    UNIQUE  KEY (spotify_id)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE playlist (
    
    id           INT UNSIGNED AUTO_INCREMENT NOT NULL,
    spotify_id   VARCHAR(30) NOT NULL,
    country_code VARCHAR(3) NOT NULL,

    PRIMARY KEY (id),
    UNIQUE  KEY (spotify_id),

    KEY idx_fk_country_code (country_code),
    CONSTRAINT fk_playlist_country_code FOREIGN KEY (country_code) REFERENCES country(country_code) ON DELETE RESTRICT ON UPDATE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE playlist_item (
    
    id          INT UNSIGNED AUTO_INCREMENT NOT NULL,
    playlist_id VARCHAR(30) NOT NULL,
    item_id     VARCHAR(30) NOT NULL,

    PRIMARY KEY (id),

    KEY idx_fk_playlist_id (playlist_id),
    KEY idx_fk_item_id (item_id),
    CONSTRAINT fk_playlist_item_playlist_id FOREIGN KEY (playlist_id) REFERENCES playlist(spotify_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_playlist_item_item_id FOREIGN KEY (item_id) REFERENCES song(spotify_id) ON DELETE RESTRICT ON UPDATE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
