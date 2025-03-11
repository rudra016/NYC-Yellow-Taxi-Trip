import os
import pandas as pd

def clean_data(input_path, output_path):
    """Clean and preprocess NYC Yellow Taxi data file by file."""
    os.makedirs(output_path, exist_ok=True)

    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_path, filename)
            df_iter = pd.read_csv(file_path, chunksize=100000)  # Process in chunks

            for chunk in df_iter:
                # ✅ Normalize column names to lowercase
                chunk.columns = chunk.columns.str.lower()

                # ✅ Drop duplicates and NaN values
                chunk.drop_duplicates(inplace=True)
                chunk.dropna(inplace=True)

                # ✅ Ensure `fare_amount` and `trip_distance` are positive
                chunk = chunk[(chunk['fare_amount'] > 0) & (chunk['trip_distance'] > 0)]

                # ✅ Remove rows with invalid `passenger_count`
                chunk = chunk[chunk['passenger_count'] >= 1]

                # ✅ Convert `store_and_fwd_flag` to standardized values ('1' or '0')
                chunk['store_and_fwd_flag'] = (chunk['store_and_fwd_flag'] == 'Y').astype(int)

                # ✅ Convert timestamps to proper datetime format
                chunk['tpep_pickup_datetime'] = pd.to_datetime(chunk['tpep_pickup_datetime'], errors='coerce')
                chunk['tpep_dropoff_datetime'] = pd.to_datetime(chunk['tpep_dropoff_datetime'], errors='coerce')

                # ✅ Remove rows where pickup is after dropoff
                chunk = chunk[chunk['tpep_pickup_datetime'] < chunk['tpep_dropoff_datetime']]

                # ✅ Remove unrealistic dates (before 2000 or in the future)
                chunk = chunk[(chunk['tpep_pickup_datetime'].dt.year >= 2000) & 
                              (chunk['tpep_pickup_datetime'].dt.year <= 2025)]

                # ✅ Fill missing `ratecodeid` with 1 (Standard Rate)
                chunk['ratecodeid'].fillna(1, inplace=True)

                # ✅ Write cleaned data to output CSV (append mode to avoid overwriting)
                output_file = os.path.join(output_path, filename)
                chunk.to_csv(output_file, mode="a", header=not os.path.exists(output_file), index=False)

            print(f"✅ Cleaned data saved to {output_file}")
