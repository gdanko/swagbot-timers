/* sqlite3 swagbot/data/timers.db < schema.sql */

DROP TABLE IF EXISTS timers;
CREATE TABLE timers (
  title TEXT NOT NULL PRIMARY KEY UNIQUE,
  description TEXT NOT NULL,
  expires INTEGER NOT NULL,
  expired INTEGER NOT NULL
);
