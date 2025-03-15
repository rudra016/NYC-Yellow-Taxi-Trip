# NYC TAXI TRIP DATASET

## About Dataset

### Context
New York City (NYC) Taxi & Limousine Commission (TLC) keeps data from all its cabs, and it is freely available to download from its official website. You can access it here. Now, the TLC primarily keeps and manages data for 4 different types of vehicles:

- **Yellow Taxi: Yellow Medallion Taxicabs:** These are the famous NYC yellow taxis that provide transportation exclusively through street hails. The number of taxicabs is limited by a finite number of medallions issued by the TLC. You access this mode of transportation by standing in the street and hailing an available taxi with your hand. The pickups are not pre-arranged.
- **Green Taxi: Street Hail Livery:** The SHL program will allow livery vehicle owners to license and outfit their vehicles with green borough taxi branding, meters, credit card machines, and ultimately the right to accept street hails in addition to pre-arranged rides.
- **For-Hire Vehicles (FHVs):** FHV transportation is accessed by a pre-arrangement with a dispatcher or limo company. These FHVs are not permitted to pick up passengers via street hails, as those rides are not considered pre-arranged.

## Data fields

● id - a unique identifier for each trip

● vendorID - a code indicating the provider associated with the trip record

● tpep_pickup_datetime -	The date and time when the meter was engaged.

● tpep_dropoff_datetime -	The date and time when the meter was disengaged.

● Trip_distance -	The elapsed trip distance in miles reported by the taximeter.

● RateCodeID -	The final rate code in effect at the end of the trip.

● passenger_count - the number of passengers in the vehicle (driver entered value)

● pickup_longitude - the longitude where the meter was engaged

● pickup_latitude - the latitude where the meter was engaged

● dropoff_longitude - the longitude where the meter was disengaged

● dropoff_latitude - the latitude where the meter was disengaged

● store_and_fwd_flag - This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server - Y=store and forward; N=not a store and forward trip

● Payment_type -	A numeric code signifying how the passenger paid for the trip.

● Fare_amount -	The time-and-distance fare calculated by the meter.

● Extra -	Miscellaneous extras and surcharges. Currently, this only includes. the $0.50 and $1 rush hour and overnight charges.

● MTA_tax -	0.50 MTA tax that is automatically triggered based on the metered rate in use.

● Improvement_surcharge -	0.30 improvement surcharge assessed trips at the flag drop. the improvement surcharge began being levied in 2015.

● Tip_amount - Tip amount – This field is automatically populated for credit card tips.Cash tips are not included.

● Tolls_amount - Total amount of all tolls paid in trip.

● Total_amount - The total amount charged to passengers. Does not include cash tips.

## ETL Pipeline using Apache Airflow

This repository contains an ETL (Extract, Transform, Load) pipeline built using Apache Airflow. The pipeline automates the process of data extraction, transformation, and loading into a database or data warehouse.

### Prerequisites
Before running the pipeline, ensure you have the following installed:

- Docker
- Astro CLI (Astronomer)

### Setup and Running the Pipeline
- Clone the Repository
 ```
  git clone https://github.com/rudra016/NYC-Yellow-Taxi-Trip.git
  cd etl-pipeline
  ```
- Install Dependencies using:
  ```
  pip install -r requirements.txt
  ```

- Start the Airflow Environment
  ```
  astro dev start
  ```
- This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

  - Postgres: Airflow's Metadata Database
  - Webserver: The Airflow component responsible for rendering the Airflow UI
  - Scheduler: The Airflow component responsible for monitoring and triggering tasks
  - Triggerer: The Airflow component responsible for triggering deferred tasks
    
- Access the Airflow UI
  Once started, open your browser and go to:
  ```
  http://localhost:8080
  ```
  Use the default Airflow credentials:

  ```
  Username: admin
  Password: admin
  ```
- Trigger the ETL DAG
- Navigate to the Airflow UI
- Locate your ETL DAG
- Click "Trigger DAG" to start execution

- Stopping the Environment
  To stop the Airflow environment, run:
  ```
  astro dev stop
  ```

### Log Files of a Successful DAG Run
For the purpose of this assignment, three log files have been manually downloaded and added to the repository. These logs confirm the successful execution of each ETL step:

 - logfiles-etl-pipeline/extract.log – Log file showing successful data extraction.
 - logfiles-etl-pipeline/transform.log – Log file showing successful data transformation.
 - logfiles-etl-pipeline/load.log – Log file showing successful data loading.

### Data Analysis and Visualization
After running the ETL pipeline, data analysis and visualization have been performed. The Jupyter Notebook for this analysis is available in:
```
data-analysis:visualization notebook/
```
You can open the notebook to explore insights, visualizations, and further analysis based on the processed data.
