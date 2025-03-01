import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'etl_e6515f-postgres-1',  # Use Docker service name
    'port': '5432'
}

TABLE_NAME = "nyc_taxi_data"

def load_data_to_postgres(input_path):
    """Load cleaned data into PostgreSQL in batches."""
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # ✅ Alter table to add missing columns if they don't exist
    alter_table_query = f"""
    ALTER TABLE {TABLE_NAME} 
    ADD COLUMN IF NOT EXISTS pickup_longitude DOUBLE PRECISION,
    ADD COLUMN IF NOT EXISTS pickup_latitude DOUBLE PRECISION,
    ADD COLUMN IF NOT EXISTS dropoff_longitude DOUBLE PRECISION,
    ADD COLUMN IF NOT EXISTS dropoff_latitude DOUBLE PRECISION;
    """
    cursor.execute(alter_table_query)
    conn.commit()

    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_path, filename)
            df_iter = pd.read_csv(file_path, chunksize=50000)

            for chunk in df_iter:
                # ✅ Rename columns to match PostgreSQL table (fix case issues)
                chunk.columns = chunk.columns.str.lower()

                # ✅ Ensure the column order exactly matches PostgreSQL table
                expected_columns = [
                    'vendorid', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
                    'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude',
                    'ratecodeid', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude',
                    'payment_type', 'fare_amount', 'extra', 'mta_tax',
                    'tip_amount', 'tolls_amount', 'improvement_surcharge',
                    'total_amount'
                ]
                
                for col in expected_columns:
                    if col not in chunk.columns:
                        chunk[col] = None  

                chunk = chunk[expected_columns]
                # ✅ Convert DataFrame to list of tuples for batch insert
                records_list = list(chunk.itertuples(index=False, name=None))

                insert_query = f"""
                INSERT INTO {TABLE_NAME} (
                    VendorID, tpep_pickup_datetime, tpep_dropoff_datetime,
                    passenger_count, trip_distance, pickup_longitude, pickup_latitude,
                    ratecodeid, store_and_fwd_flag, dropoff_longitude, dropoff_latitude,
                    payment_type, fare_amount, extra, mta_tax,
                    tip_amount, tolls_amount, improvement_surcharge,
                    total_amount
                ) VALUES %s
                ON CONFLICT DO NOTHING;
                """

                execute_values(cursor, insert_query, records_list)
                conn.commit()

    cursor.close()
    conn.close()
    print("✅ Data successfully loaded into PostgreSQL.")
