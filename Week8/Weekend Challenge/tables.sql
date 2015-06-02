CREATE TABLE IF NOT EXISTS InternalLinks(
    id INTEGER PRIMARY KEY,
    url TEXT,
    visited INTEGER
);

CREATE TABLE IF NOT EXISTS ExternalLinksAndServers(
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE,
    server TEXT
);
