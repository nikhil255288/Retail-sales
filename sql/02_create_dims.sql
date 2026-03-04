CREATE SCHEMA IF NOT EXISTS dw;

CREATE TABLE IF NOT EXISTS dw.dim_date (
  date_id   INT PRIMARY KEY,          -- e.g., 20260303
  full_date DATE UNIQUE NOT NULL,
  day       INT NOT NULL,
  month     INT NOT NULL,
  quarter   INT NOT NULL,
  year      INT NOT NULL
);

CREATE TABLE IF NOT EXISTS dw.dim_product (
  product_id    SERIAL PRIMARY KEY,
  product_code  TEXT UNIQUE NOT NULL,
  product_name  TEXT,
  category      TEXT,
  brand         TEXT
);

CREATE TABLE IF NOT EXISTS dw.dim_customer (
  customer_id    SERIAL PRIMARY KEY,
  customer_code  TEXT UNIQUE NOT NULL,
  gender         TEXT,
  age_group      TEXT,
  city           TEXT
);

CREATE TABLE IF NOT EXISTS dw.dim_store (
  store_id     SERIAL PRIMARY KEY,
  store_code   TEXT UNIQUE NOT NULL,
  store_name   TEXT,
  region       TEXT,
  state        TEXT
);
