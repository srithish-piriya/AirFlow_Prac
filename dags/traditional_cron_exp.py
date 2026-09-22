from airflow.sdk import dag,task
from airflow.timetables.trigger import CronTriggerTimetable
from pendulum import datetime
@dag(dag_id ="cron_trad_dag",
     start_date =datetime(year=2026,month=9,day=1,tz="Asia/Kolkata"),
     end_date=datetime(year=2026,month=9,day=30,tz="Asia/Kolkata"),
     schedule="0 0 * * 0-5",
     is_paused_upon_creation = False,
     catchup = True)
def cron_trad_dag():
    @task.python
    def first_task():
        print("Hello Word")
    @task.python
    def second_task():
        print("kjdn")
    @task.python
    def third_task():
        print("kjjhbjdn")
     
    #defing task dependendencies 
    first = first_task()
    sec = second_task()
    third = third_task()
    first >> sec >> third
cron_trad_dag()