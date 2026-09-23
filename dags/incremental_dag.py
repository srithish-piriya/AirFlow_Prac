from airflow.sdk import dag,task
from pendulum import datetime
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(dag_id="incremental_dag",
     schedule=CronDataIntervalTimetable(cron="0 0 * * *", timezone="Asia/Kolkata"),
     start_date = datetime(year=2026,month=9,day=21,tz="Asia/Kolkata"),
     end_date = datetime(year=2026,month=9,day=23,tz="Asia/Kolkata"),
     catchup = True,
     is_paused_upon_creation = False)
def incremental_dag():
    @task.python
    def date_fetch(**kwargs):
        date_interval_start =kwargs['data_interval_start']
        date_interval_end =kwargs['data_interval_end']
        print(f"date interval start is {date_interval_start}")
    @task.bash
    def date_fetch_bash():
        return "echo 'date interval start is {{data_interval_start}} and date interval end is {{data_interval_end}}'"
    first = date_fetch()
    second = date_fetch_bash()
    first >> second
incremental_dag()