CREATE TABLE IF NOT EXISTS ex06_movies (
    episode_nb INT PRIMARY KEY,
    title VARCHAR(64) UNIQUE NOT NULL,
    opening_crawl TEXT,
    director VARCHAR(32) NOT NULL,
    producer VARCHAR(128) NOT NULL,
    release_date DATE NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creating a function to update the changetimestamp column on update
CREATE OR REPLACE FUNCTION update_changetimestamp_column()
RETURNS TRIGGER AS $$
BEGIN
NEW.updated = now();
NEW.created = OLD.created;
RETURN NEW;
END;
$$ language 'plpgsql';

-- Creating the trigger to call the function on update
CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE -- When it gets triggeres
ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE -- the scope of the trigger
update_changetimestamp_column(); -- what does the trigger do