-- Create a table and returns no error if the table exists
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INt DEFAULT 1 UNIQUE, `name` VARCHAR(256));
