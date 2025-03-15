## Objective: Build a comprehensive data pipeline for an urban mobility analytics platform.
### Dataset: [Use the NYC Taxi & Limousine Commission Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data).
### Tasks:
 - Data Ingestion: Write ETL jobs (Python scripts or Airflow DAGs) to ingest raw data, clean it, and store it in a data warehouse (PostgreSQL or Amazon Redshift).
 - Data Analysis: Perform advanced analysis (e.g., trip duration predictions, hotspot analysis) using Pandas and NumPy.
 - Visualization: Create interactive dashboards using Plotly/Dash that showcase key metrics (heat maps, time‑series plots).
### Requirements: Make sure to include the following in your final submission:
- Group-By Operations: Group the data by the newly created time features (e.g., hour) and compute aggregate metrics like mean trip duration and total trip count.
- Pivot Tables: Create a pivot table that shows aggregated metrics (e.g., average trip duration) across different days of the week and hours Simulated Weather Data: Create or use a small CSV file that simulates hourly weather data (temperature, precipitation, etc.) for the same period.
- Vectorized Computations: Identify a loop-based operation in your cleaning or feature engineering steps and replace it with a NumPy vectorized solution (e.g., using np.where, or vectorized arithmetic).
- Lambda Functions & Apply: Use DataFrame.apply() with lambda functions to compute a custom metric (e.g., a risk score based on trip duration and distance).
- Execution Time Comparison: Measure and compare the execution time of your loop-based approach versus the vectorized implementation (using Python’s time module or %timeit in a Jupyter Notebook).
- Deliverables: A GitHub repository containing the ETL pipeline code, dashboards, Jupyter Notebooks with analysis, and detailed documentation.
