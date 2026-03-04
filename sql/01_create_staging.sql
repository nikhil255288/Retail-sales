CREATE SCHEMA IF NOT EXISTS stg;

CREATE TABLE IF NOT EXISTS stg.sales_raw (
  sales_id         TEXT,
  sale_date        DATE,
  product_code     TEXT,
  customer_code    TEXT,
  store_code       TEXT,
  quantity         INT,
  revenue          NUMERIC(12,2),
  discount         NUMERIC(12,2),
  profit           NUMERIC(12,2),
  order_id         TEXT
);

CREATE TABLE IF NOT EXISTS stg.product_raw (
  product_code   TEXT PRIMARY KEY,
  product_name   TEXT,
  category       TEXT,
  brand          TEXT
);

CREATE TABLE IF NOT EXISTS stg.customer_raw (
  customer_code  TEXT PRIMARY KEY,
  gender         TEXT,
  age_group      TEXT,
  city           TEXT
);

CREATE TABLE IF NOT EXISTS stg.store_raw (
  store_code     TEXT PRIMARY KEY,
  store_name     TEXT,
  region         TEXT,
  state          TEXT
);
