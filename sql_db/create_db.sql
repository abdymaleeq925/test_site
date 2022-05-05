CREATE DATABASE practice_site;
CREATE USER site_user WITH PASSWORD '321tset';
ALTER ROLE site_user SET client_encoding TO 'utf-8';
ALTER ROLE site_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE site_user SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE practice_site TO site_user;