-- Select the alx_book_store database (passed as an argument in mysql command)
USE alx_book_store;

-- Query the INFORMATION_SCHEMA to get the column details of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
