CREATE TABLE IF NOT EXISTS ex08_planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    climate VARCHAR,
    diameter INT,
    orbital_period INT,
    population BIGINT,
    rotation_period INT,
    surface_water REAL,
    terrain VARCHAR(128)
);

CREATE TABLE IF NOT EXISTS ex08_people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL,
    birth_year VARCHAR(32),
    gender VARCHAR(32),
    eye_color VARCHAR(32),
    hair_color VARCHAR(32),
    height INT,
    mass REAL,
    homeworld VARCHAR(64) REFERENCES ex08_planets(name)
);
