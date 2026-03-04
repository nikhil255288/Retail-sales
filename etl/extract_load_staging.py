import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

from config import DB

# Folder where your generated CSVs live
DATA_DIR = Path("data/raw")

# stg table name  -> csv file name
FILES = {
    "product_raw": "products.csv",
    "customer_raw": "customers.csv",
    "store_raw": "stores.csv",
    "sales_raw": "sales.csv",
}


def pg_engine():
    url = (
        f"postgresql+psycopg2://{DB['user']}:{DB['password']}"
        f"@{DB['host']}:{DB['port']}/{DB['database']}"
    )
    return create_engine(url, future=True)


def load_one(engine, table: str, csv_name: str) -> int:
    path = DATA_DIR / csv_name

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path.resolve()}")

    df = pd.read_csv(path)

    # wipe staging each run so you don't double-load
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE stg.{table};"))

    # load into Postgres
    df.to_sql(
        name=table,
        con=engine,
        schema="stg",
        if_exists="append",
        index=False,
        method="multi",
        chunksize=2000,
    )

    return len(df)


def main():
    engine = pg_engine()

    # connection test
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    total = 0
    for table, csv_name in FILES.items():
        rows = load_one(engine, table, csv_name)
        total += rows
        print(f"✅ Loaded {rows:,} rows into stg.{table} from {csv_name}")

    print(f"🎉 Staging load complete. Total rows loaded: {total:,}")


if __name__ == "__main__":
    main()