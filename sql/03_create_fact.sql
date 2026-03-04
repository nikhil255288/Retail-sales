CREATE TABLE IF NOT EXISTS dw.fact_sales (
  sales_sk    BIGSERIAL PRIMARY KEY,
  sales_id    TEXT,
  order_id    TEXT,
  date_id     INT NOT NULL REFERENCES dw.dim_date(date_id),
  product_id  INT NOT NULL REFERENCES dw.dim_product(product_id),
  customer_id INT NOT NULL REFERENCES dw.dim_customer(customer_id),
  store_id    INT NOT NULL REFERENCES dw.dim_store(store_id),
  quantity    INT NOT NULL,
  revenue     NUMERIC(12,2) NOT NULL,
  discount    NUMERIC(12,2) NOT NULL,
  profit      NUMERIC(12,2) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_fact_date ON dw.fact_sales(date_id);
CREATE INDEX IF NOT EXISTS idx_fact_product ON dw.fact_sales(product_id);
CREATE INDEX IF NOT EXISTS idx_fact_store ON dw.fact_sales(store_id);
CREATE INDEX IF NOT EXISTS idx_fact_customer ON dw.fact_sales(customer_id);
