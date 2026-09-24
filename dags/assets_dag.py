from airflow.sdk import asset
import os


@asset(
    name="fetch_data",
    schedule="@daily",
    uri="/opt/airflow/logs/data/data_extract.txt"
)
def fetch_data(self):

    # Create parent directory
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    # Write data to file
    with open(self.uri, "w") as f:
        f.write("data fetched successfully")

    print(f"Data written to {self.uri}")