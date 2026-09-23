from airflow.sdk import dag,task,asset
from pendulum import datetime
import os

@asset(name="fetch_data",
       schedule="@daily",
       is_paused_upon_creation=False,
       uri = '/opt/airflow/logs/data/data_extract.txt'
       )
def fetch_data(self):
    #creating a directory to store data
    os.makedirs(self.uri,exist_ok=True)

    #loading data into the file
    with open(self.uri,'w') as f:
        f.write(f'data fetched on {datetime.now('asia/Kolkata')}')
    print(f'data written to {self.uri} on {datetime.now("Asia/Kolkata")}')