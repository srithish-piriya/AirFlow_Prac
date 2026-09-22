from airflow.sdk import dag,task
from  pendulum  import datetime
@dag(dag_id="schedule_dag",
    start_date = datetime(year = 2026 ,month =9 ,day= 22,tz="Asia/Kolkata"),
    schedule="@daily",is_paused_upon_creation = False)
def schedule_dag():
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
#instantiating the dag
schedule_dag()      