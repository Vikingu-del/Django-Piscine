CREATE TABLE IF NOT EXISTS ex04_movies (
    episode_nb INT PRIMARY KEY,
    title VARCHAR(64) UNIQUE NOT NULL,
    opening_crawl TEXT,
    director VARCHAR(32) NOT NULL,
    producer VARCHAR(128) NOT NULL,
    release_date DATE NOT NULL
)
