DROP TABLE IF EXISTS request_logs;
DROP TABLE IF EXISTS cache_entries;
DROP TABLE IF EXISTS routing_rules;

SOURCE db/schema.sql;
SOURCE db/seed_demo.sql;
