import os
import kagglehub
import zipfile

DATASET = "elemento/nyc-yellow-taxi-trip-data"

def download_data(save_path):
    """Download NYC Yellow Taxi dataset from Kaggle in chunks."""
    os.makedirs(save_path, exist_ok=True)

    print("Starting dataset download...")
    path = kagglehub.dataset_download(DATASET)

    print(f"Dataset downloaded to: {path}")

    # Unzip files directly into the raw data folder
    for file in os.listdir(path):
        if file.endswith(".csv"):
            full_path = os.path.join(path, file)
            os.rename(full_path, os.path.join(save_path, file))
            print(f"Extracted: {file}")

    print(f"All files moved to: {save_path}")
