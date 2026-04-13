CREATE TABLE IF NOT EXISTS ex00_movies (
    episode_nb INT PRIMARY KEY,
    title VARCHAR(64) UNIQUE NOT NULL,
    opening_crawl TEXT,
    director VARCHAR(32) NOT NULL,
    producer VARCHAR(128) NOT NULL,
    releace_date DATE NOT NULL
)