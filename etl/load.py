import psycopg2
from psycopg2 import sql

def load_data(data: pd.DataFrame, table_name: str, db_config: dict):
    """
    Load data into a PostgreSQL database.
    """
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute(sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            product_id INT PRIMARY KEY,
            total_sales FLOAT
        );
    """).format(sql.Identifier(table_name)))

    # Insert data
    for _, row in data.iterrows():
        cursor.execute(sql.SQL("""
            INSERT INTO {} (product_id, total_sales)
            VALUES (%s, %s)
            ON CONFLICT (product_id) DO UPDATE
            SET total_sales = EXCLUDED.total_sales;
        """).format(sql.Identifier(table_name)), (row["product_id"], row["sales"]))

    conn.commit()
    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    from transform import transform_data
    from extract import extract_data

    db_config = {
        "dbname": "retail_warehouse",
        "user": "postgres",
        "password": "password",
        "host": "localhost",
        "port": 5432,
    }

    data = extract_data("data/raw/sales_data.csv")
    transformed_data = transform_data(data)
    load_data(transformed_data, "sales_summary", db_config)