CREATE USER IF NOT EXISTS 'pyuser'@'localhost' IDENTIFIED BY 'Py@pp4Demo';

GRANT ALL PRIVILEGES ON dataengineering.* TO 'pyuser'@'localhost';
GRANT ALL PRIVILEGES ON test.* TO 'pyuser'@'localhost';
GRANT ALL PRIVILEGES ON production.* TO 'pyuser'@'localhost';
