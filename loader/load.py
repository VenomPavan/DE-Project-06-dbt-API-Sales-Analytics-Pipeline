from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "pavan"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "sales_dbt"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def load_to_postgres(df, table_name):
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")