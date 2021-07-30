CREATE TABLE IF NOT EXISTS csvfile (
        batch varchar(20) PRIMARY KEY,
        start datetime NOT NULL DEFAULT current_timestamp,
        end datetime NOT NULL DEFAULT current_timestamp,
        records INTEGER NOT NULL,
        pass BOOLEAN,
        message VARCHAR(100)
);
